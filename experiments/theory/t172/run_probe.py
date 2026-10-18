"""Small actual-meter development probe with preserved outputs and costs."""
from pathlib import Path
from importlib import metadata
import importlib.util,hashlib,json,os,re,resource,sys,time
import numpy as np
import flopscope as flops
from whestbench import MLP,SetupContext
B=Path(__file__).resolve().parent;R=B.parents[2]
name=sys.argv[1];rows=list(map(int,sys.argv[2:]));source=B/'sources'/name
cfg=json.loads((source/'CONFIG.json').read_text());f=source/'estimator.py'
assert hashlib.sha256(f.read_bytes()).hexdigest()==cfg['source_sha256']
if cfg.get('asset_sha256'):
 assert hashlib.sha256((source/'nn_asset.json').read_bytes()).hexdigest()==cfg['asset_sha256']
out=B/'runs'/name;out.mkdir(parents=True,exist_ok=False)
for key in set(re.findall(r'_os.environ.get\("([^"]+)"',f.read_text())):os.environ.pop(key,None)
sp=importlib.util.spec_from_file_location('candidate',f);mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
inputs={}
for manifest in ['experiments/theory/t163/P30_INPUT_MANIFEST.json','experiments/submission_policy/t171/INPUT_MANIFEST.json','experiments/submission_policy/t171/EXTENSION_INPUT_MANIFEST.json']:
 for rec in json.loads((R/manifest).read_text())['records']:
  if (R/rec['path']).exists():inputs[rec['row']]=rec
assert set(rows)<=set(inputs),set(rows)-set(inputs)
def arrayhash(x):
 x=np.ascontiguousarray(x);h=hashlib.sha256();h.update(x.dtype.str.encode());h.update(json.dumps(x.shape).encode());h.update(x.tobytes());return h.hexdigest()
est=mod.Estimator();t=time.perf_counter();est.setup(SetupContext(width=1024,depth=16,flop_budget=2**41,api_version='2.0',submission_dir=str(source),seed=0));setup=time.perf_counter()-t
start=dict(config=cfg,rows=rows,start_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),data_role='Previously exposed public development, adaptive research permitted.',runtime=dict(python=sys.version,**{x:metadata.version(x) for x in ['flopscope','flopscope-server','whestbench','numpy']}),seed_protocol='2.0; same recorded public inputs as historical comparisons; shipped estimator uses no per-MLP RNG')
(out/'START.json').write_text(json.dumps(start,indent=2)+'\n');records=[]
for call,row in enumerate(rows):
 rec=inputs[row];weights=np.load(R/rec['path'],allow_pickle=False);assert arrayhash(weights)==rec['weights_sha256']
 mlp=MLP.from_row({'weights':weights,'mlp_seed':rec['mlp_seed']},seed_protocol_version='2.0');del weights
 t=time.perf_counter()
 try:
  with flops.BudgetContext(flop_budget=2**41,wall_time_limit_s=120.,quiet=True) as ctx:pred=est.predict(mlp,2**41)
  pred=np.asarray(pred,dtype=np.float32).copy();outer=time.perf_counter()-t
  meter=dict(flops=int(ctx.flops_used),wall_time_s=float(ctx.wall_time_s),residual_wall_time_s=float(ctx.residual_wall_time_s),outer_wall_time_s=outer)
 except Exception as e:
  (out/'ERROR.json').write_text(json.dumps(dict(call=call,row=row,type=type(e).__name__,message=str(e)),indent=2)+'\n');raise
 finite=pred.shape==(16,1024) and bool(np.isfinite(pred).all());rss=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024
 np.savez_compressed(out/f'PREDICTION-{call:02d}-{row}.npz',prediction=pred)
 record=dict(call=call,row=row,meter=meter,setup_s=setup,peak_rss_bytes=rss,prediction_sha256=arrayhash(pred),checks=dict(finite=finite,flops=meter['flops']<=2**41,residual=meter['residual_wall_time_s']<.4,wall=outer<120,memory=rss<2**33,setup=setup<5))
 if row>=750:
  target=np.load(R/'experiments/checkpoint3/t118'/('VD_TARGETS.npz' if row<850 else 'H_TARGETS.npz'))['targets'][row-(750 if row<850 else 850)]
  raw=float(np.mean((pred[-1].astype(float)-target.astype(float))**2));record.update(raw_mse=raw,adjusted_mse=raw*max(.1,meter['flops']/2**41))
 (out/f'CALL-{call:02d}.json').write_text(json.dumps(record,indent=2)+'\n');records.append(record);print(json.dumps(record),flush=True);del mlp
 if not finite:break
result=dict(probe=name,records=records,complete=len(records)==len(rows),all_caps_pass=all(all(r['checks'].values()) for r in records))
if all('raw_mse' in r for r in records):result.update(mean_raw=float(np.mean([r['raw_mse'] for r in records])),mean_adjusted=float(np.mean([r['adjusted_mse'] for r in records])))
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='records'}),flush=True)
