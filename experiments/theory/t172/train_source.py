"""P14: fixed local-innovation learning on P13's cheaper physical trajectory.

Two justified feature families, identical15→32→4 or24→32→4 architecture,
1000updates, four whole-network folds plus final all32fit. Conditional/adaptive
CV: the frozen physical covariance coefficients already use these32networks.
"""
from pathlib import Path
import json,hashlib,time,numpy as np,torch
B=Path(__file__).resolve().parent;R=B.parents[2]
run=json.loads((B/'P13_CAPTURE/RESULT.json').read_text());assert run['complete'];rows=run['config']['rows'];N=len(rows);assert N==32
out=B/'P14_FIT';out.mkdir(exist_ok=True);torch.set_num_threads(4)
labelrec=json.loads((B.parent/'t166/P35_LABEL_MANIFEST.json').read_text());lp=R/labelrec['path'];assert hashlib.sha256(lp.read_bytes()).hexdigest()==labelrec['sha256'];labels=np.load(lp)['labels'].astype(float);assert labelrec['rows']==rows
features=[];extra=[];gate=[];amp=[];full=[]
for rec in run['records']:
 path=R/rec['capture_path'];assert hashlib.sha256(path.read_bytes()).hexdigest()==rec['capture_sha256'];z=np.load(path)
 features.append(z['features']);extra.append(z['extra']);gate.append(z['gate']);amp.append(z['amp']);full.append(z['prediction'])
features=np.asarray(features,dtype=float);extra=np.asarray(extra,dtype=float);gate=np.asarray(gate,dtype=float);amp=np.asarray(amp,dtype=float);full=np.asarray(full,dtype=float)
inputs={r['row']:r for r in json.loads((B.parent/'t163/P30_INPUT_MANIFEST.json').read_text())['records']}
weights=np.asarray([np.load(R/inputs[row]['path'])[1:] for row in rows],dtype=np.float32)
e=labels-full;src=np.empty((N,15,1024));check=e[:,0].copy()
for t in range(15):
 src[:,t]=e[:,t+1]-gate[:,t]*np.einsum('bji,bj->bi',weights[:,t],e[:,t])
 check=gate[:,t]*np.einsum('bji,bj->bi',weights[:,t],check)+src[:,t]
identity=float(np.max(abs(check-e[:,-1])));assert identity<1e-12
blocks=np.array([0]*5+[1]*5+[2]*4+[3]);ix=np.arange(N);block_all=torch.tensor(np.broadcast_to(blocks[None,:,None],(N,15,1024)).copy().reshape(-1))
def propagate(s):
 state=np.zeros((N,1024))
 for t in range(15):state=gate[:,t]*np.einsum('bji,bj->bi',weights[:,t],state)+s[:,t]
 return state
class Source(torch.nn.Module):
 def __init__(self,width):
  super().__init__();self.hidden=torch.nn.Linear(width,32);self.output=torch.nn.Linear(32,4);torch.nn.init.zeros_(self.output.weight);torch.nn.init.zeros_(self.output.bias)
 def forward(self,x,b):return self.output(torch.tanh(self.hidden(x))).gather(1,b[:,None])[:,0]
base=np.mean((labels[:,-1]-full[:,-1])**2,axis=1);results={};all_cv={}
for family,xx in [('local15',features),('trace24',np.concatenate([features,extra],axis=-1))]:
 width=xx.shape[-1];cv=full[:,-1].copy();records=[]
 for fold in [0,1,2,3,None]:
  name=str(fold) if fold is not None else 'ALL';path=out/f'{family}-{name}.json';prediction_path=out/f'{family}-{name}.npz'
  tr=ix if fold is None else ix[ix%4!=fold];te=ix if fold is None else ix[ix%4==fold]
  if path.exists() and prediction_path.exists():
   rec=json.loads(path.read_text());pred=np.load(prediction_path)['prediction'];records.append(rec)
   if fold is not None:cv[te]=pred[te]
   continue
  start=time.time();mean=xx[tr].mean((0,1,2));std=np.maximum(xx[tr].std((0,1,2)),1e-12);x=np.clip((xx-mean)/std,-8,8).astype(np.float32)
  torch.manual_seed(172014+(fold if fold is not None else 4));model=Source(width);opt=torch.optim.Adam(model.parameters(),lr=.01)
  tx=torch.from_numpy(x[tr].reshape(-1,width));tb=torch.tensor(np.broadcast_to(blocks[None,:,None],(len(tr),15,1024)).copy().reshape(-1));ta=torch.from_numpy(amp[tr].reshape(-1).astype(np.float32));ty=torch.from_numpy(src[tr].reshape(-1).astype(np.float32))
  scale=np.maximum(np.sqrt(np.mean(src[tr]**2,(0,2))),1e-8);ts=torch.from_numpy(np.broadcast_to(scale[None,:,None],(len(tr),15,1024)).copy().reshape(-1).astype(np.float32));gen=torch.Generator().manual_seed(172114+(fold if fold is not None else 4));curves=[]
  for step in range(1,1001):
   jj=torch.randint(len(ty),(32768,),generator=gen);opt.zero_grad();got=.001*ta[jj]*model(tx[jj],tb[jj]);loss=torch.mean(((got-ty[jj])/ts[jj])**2)+1e-4*sum(torch.sum(p*p) for p in model.parameters())/sum(p.numel() for p in model.parameters());loss.backward();torch.nn.utils.clip_grad_norm_(model.parameters(),5.);opt.step()
   if step%250==0:
    rec=dict(family=family,fold=fold,step=step,training_batch_loss=float(loss.detach()),seconds=time.time()-start);curves.append(rec);print(json.dumps(rec),flush=True)
  with torch.no_grad():raw=model(torch.from_numpy(x.reshape(-1,width)),block_all).numpy().reshape(N,15,1024)
  pred=np.maximum(full[:,-1]+propagate(.001*amp*raw),0)
  if fold is not None:cv[te]=pred[te]
  d=model.state_dict();asset=dict(mean=mean.tolist(),scale=std.tolist(),hw=d['hidden.weight'].numpy().tolist(),hb=d['hidden.bias'].numpy().tolist(),ow=d['output.weight'].numpy().tolist(),ob=d['output.bias'].numpy().tolist())
  ap=out/f'{family}-{name}-asset.json';ap.write_text(json.dumps(asset)+'\n');np.savez_compressed(prediction_path,prediction=pred)
  rec=dict(family=family,fold=fold,training_rows=[rows[i] for i in tr],test_rows=[] if fold is None else [rows[i] for i in te],steps=1000,seconds=time.time()-start,asset_sha256=hashlib.sha256(ap.read_bytes()).hexdigest(),curves=curves,terminal_ratio_on_test=float(np.mean((pred[te]-labels[te,-1])**2)/base[te].mean()))
  path.write_text(json.dumps(rec,indent=2)+'\n');records.append(rec);print(json.dumps({k:v for k,v in rec.items() if k not in ['curves','training_rows','test_rows']}),flush=True)
  del model,opt,tx,tb,ta,ty,ts
 mse=np.mean((cv-labels[:,-1])**2,axis=1);results[family]=dict(mean_mse=float(mse.mean()),baseline_mean=float(base.mean()),ratio=float(mse.mean()/base.mean()),wins=int((mse<base).sum()),per_network_mse=mse.tolist(),records=records);all_cv[family]=cv
 print(json.dumps({k:v for k,v in results[family].items() if k not in ['records','per_network_mse']},sort_keys=True),flush=True)
np.savez_compressed(out/'CV_PREDICTIONS.npz',rows=rows,base=full[:,-1],**all_cv)
result=dict(probe='P14',rows=rows,identity_max_abs=identity,results=results,role='Adaptive conditional whole-network CV on32exposedF; existing physical covariance fit uses all32. No fresh-validation or private-suite probability claim.',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),label_sha256=labelrec['sha256'])
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print('FIT COMPLETE',flush=True)
