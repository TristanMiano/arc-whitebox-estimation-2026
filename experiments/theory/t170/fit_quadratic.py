"""P27 fixed mixed+quadratic covariance dictionary ridge; no neuron-level split or hyperparameter sweep."""
from pathlib import Path
import numpy as np,json,hashlib
B=Path(__file__).resolve().parent;R=B.parents[2]
rows=json.loads((B.parent/'t166/runs/P03_train/RESULT.json').read_text())['rows']
assert all((B/f'P27_RESPONSE/CALL-{r}.json').exists() for r in rows), 'Wait for completed collector'
labels=np.load(R/'tmp/t166-layer-labels.npz');assert list(labels['rows'])==rows
truth=labels['labels'].astype(float)
inputs={r['row']:r for r in json.loads((B.parent/'t163/P30_INPUT_MANIFEST.json').read_text())['records']}
design=[];innov=[];errors=[];targets=[]
for i,row in enumerate(rows):
 d=np.load(B/f'P08_RESPONSE/ROW-{row}.npz');pred=d['native'].astype(float);pred[:-1]+=d['nn_response'][:-1]
 e=truth[i]-pred;w=np.load(R/inputs[row]['path']);local=np.load(B.parent/f't166/runs/P03_train/ROW-{row}.npz')['local_state']
 y=e[1:] - np.einsum('lij,li->lj',w[1:],e[:-1])*local[:,:,4]
 extra=np.load(B/f'P12_RESPONSE/ROW-{row}.npz');mixed=np.load(B/f'P22_RESPONSE/ROW-{row}.npz');quad=np.load(B/f'P27_RESPONSE/ROW-{row}.npz');design.append(np.concatenate([d['design'][-1],extra['design'][-1],mixed['design'][-1],quad['design'][-1]],axis=-1));innov.append(np.concatenate([d['innovations'][1:],extra['innovations'][1:],mixed['innovations'][1:],quad['innovations'][1:]],axis=-1));errors.append(e[-1]);targets.append(y)
X=np.asarray(design,dtype=float);Z=np.asarray(innov,dtype=float);Y=np.asarray(errors);U=np.asarray(targets)
out=B/'P27_FIT';out.mkdir(exist_ok=False)
results={};saved={}
for objective in ['local_and_terminal','terminal_only']:
 folds=[];oof=np.zeros_like(Y)
 for fold in list(range(4))+[None]:
  train=np.ones(32,dtype=bool) if fold is None else np.arange(32)%4!=fold
  test=~train;xt=X[train].reshape(-1,96);yt=Y[train].ravel();s_end=np.sqrt(np.mean(yt**2));a=xt/s_end/np.sqrt(len(yt));b=yt/s_end/np.sqrt(len(yt))
  if objective=='local_and_terminal':
   scales=np.sqrt(np.mean(U[train]**2,axis=(0,2)));scales=np.maximum(scales,1e-15)
   z=(Z[train]/scales[None,:,None,None]).reshape(-1,96);u=(U[train]/scales[None,:,None]).ravel()
   a=np.concatenate([a,z/np.sqrt(len(u))]);b=np.concatenate([b,u/np.sqrt(len(u))])
  G=a.T@a;rhs=a.T@b;reg=.001*np.diag(np.maximum(np.diag(G),1e-30));coef=np.linalg.solve(G+reg,rhs)
  if fold is None:
   results[objective]['whole_training_coefficients']=coef.tolist();continue
  response=np.einsum('nik,k->ni',X[test],coef);oof[test]=response
  base=np.mean(Y[test]**2,axis=1);new=np.mean((Y[test]-response)**2,axis=1)
  folds.append(dict(fold=fold,train_rows=np.asarray(rows)[train].tolist(),test_rows=np.asarray(rows)[test].tolist(),coefficients=coef.tolist(),pooled_ratio=float(new.mean()/base.mean()),row_ratios=(new/base).tolist()))
  results[objective]=dict(folds=folds)
 base=np.mean(Y**2,axis=1);new=np.mean((Y-oof)**2,axis=1)
 results[objective].update(pooled_ratio=float(new.mean()/base.mean()),row_ratios=(new/base).tolist(),wins=int(sum(new<base)),base_mean=float(base.mean()),new_mean=float(new.mean()),coefficient_fold_sd=np.std([f['coefficients'] for f in folds],axis=0).tolist())
 saved[objective]=oof
np.savez_compressed(out/'OOF.npz',rows=rows,baseline_error=Y,**saved)
res=dict(probe='P27',role='Adaptive reused training-network CV, not fresh validation',rows=rows,lambda_=0.001,results=results,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(out/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:{kk:v for kk,v in r.items() if kk in ['pooled_ratio','wins','base_mean','new_mean']} for k,r in results.items()},indent=2))
