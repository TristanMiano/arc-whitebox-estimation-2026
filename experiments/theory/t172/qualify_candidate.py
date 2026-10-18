"""SDK/package identity, small fallbacks,9actual archive calls including replay."""
from pathlib import Path
from dataclasses import asdict
from datetime import datetime,timezone
import ast,hashlib,importlib.util,json,os,re,resource,subprocess,sys,tarfile,tempfile,time
import numpy as np,flopscope as flops
from whestbench import MLP,SetupContext
from whestbench.validation import validate_package
B=Path(__file__).resolve().parent;R=B.parents[2];alg=sys.argv[1];out=B/'candidates'/alg;freeze=json.loads((out/'FREEZE.json').read_text());source=R/freeze['source_directory'];cli=R/'tmp/t172-runtime312/bin/whest'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,v):(out/name).write_text(json.dumps(v,indent=2)+'\n')
def command(args,name):
 with (out/(name+'.json')).open('w') as f,(out/(name+'.log')).open('w') as e:subprocess.run(args,stdout=f,stderr=e,check=True)
assert all(sha(source/name)==h for name,h in freeze['source_hashes'].items())
command([str(cli),'validate','--estimator',str(source/'estimator.py'),'--json'],'SDK_VALIDATION')
archive=out/(alg+'.tar.gz');command([str(cli),'package','--estimator',str(source),'--output',str(archive),'--yes','--json'],'PACKAGE')
validation=asdict(validate_package(archive));write('MANIFEST_VALIDATION.json',validation);assert validation['ok']
def arrayhash(x):
 x=np.ascontiguousarray(x);h=hashlib.sha256();h.update(x.dtype.str.encode());h.update(json.dumps(x.shape).encode());h.update(x.tobytes());return h.hexdigest()
def mod(path):
 sp=importlib.util.spec_from_file_location('shipping',path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
with tempfile.TemporaryDirectory(prefix='arc-t172-archive-') as td:
 root=Path(td);expected=set(freeze['source_hashes'])|{'manifest.json'}
 with tarfile.open(archive,'r:gz') as tar:
  members=tar.getmembers();assert {x.name for x in members}==expected
  assert all(x.isfile() and not Path(x.name).is_absolute() and '..' not in Path(x.name).parts for x in members);tar.extractall(root,filter='data')
 assert all(sha(root/name)==h for name,h in freeze['source_hashes'].items())
 tree=ast.parse((root/'estimator.py').read_text());imports=[]
 for node in ast.walk(tree):
  names=[x.name for x in node.names] if isinstance(node,ast.Import) else [node.module] if isinstance(node,ast.ImportFrom) else []
  imports+=names
 allowed={'__future__','math','flopscope','flopscope.numpy','whestbench','whestbench.domain','os','gc','re','local_engine','pathlib','json'}
 assert set(imports)<=allowed,set(imports)-allowed
 for key in set(re.findall(r'_os.environ.get\("([^"]+)"',(root/'estimator.py').read_text())):os.environ.pop(key,None)
 m=mod(root/'estimator.py');fallback=[]
 for n,L in [(1,1),(5,3),(32,6)]:
  est=m.Estimator();st=time.perf_counter();est.setup(SetupContext(width=n,depth=L,flop_budget=2**41,api_version='2.0',submission_dir=str(root),seed=0));setup=time.perf_counter()-st
  w=np.random.default_rng(172000+n).normal(size=(L,n,n)).astype(np.float32)*np.float32(np.sqrt(2/n));mlp=MLP.from_row({'weights':w,'mlp_seed':172000+n},seed_protocol_version='2.0')
  with flops.BudgetContext(flop_budget=2**41,wall_time_limit_s=120,quiet=True):pred=est.predict(mlp,2**41)
  p=np.asarray(pred);fallback.append(dict(width=n,depth=L,finite_shape=p.shape==(L,n) and bool(np.isfinite(p).all()),setup_s=setup))
 write('FALLBACK.json',fallback);assert all(x['finite_shape'] and x['setup_s']<5 for x in fallback)
 est=m.Estimator();st=time.perf_counter();est.setup(SetupContext(width=1024,depth=16,flop_budget=2**41,api_version='2.0',submission_dir=str(root),seed=0));setup=time.perf_counter()-st
 inputs={r['row']:r for r in json.loads((R/'experiments/submission_policy/t171/INPUT_MANIFEST.json').read_text())['records']};records=[];last=None
 for call,row in enumerate(freeze['archive_new_rows']):
  inp=inputs[row];w=np.load(R/inp['path']);assert arrayhash(w)==inp['weights_sha256'];mlp=MLP.from_row({'weights':w,'mlp_seed':inp['mlp_seed']},seed_protocol_version='2.0');del w
  st=time.perf_counter()
  with flops.BudgetContext(flop_budget=2**41,wall_time_limit_s=120,quiet=True) as ctx:prediction=est.predict(mlp,2**41)
  pred=np.asarray(prediction,dtype=np.float32).copy();wall=time.perf_counter()-st;rss=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024
  checks=dict(finite=pred.shape==(16,1024) and bool(np.isfinite(pred).all()),flops=ctx.flops_used<=2**41,residual=ctx.residual_wall_time_s<.4,wall=wall<120,memory=rss<2**33,setup=setup<5)
  if call==len(freeze['archive_new_rows'])-1:checks['byte_replay']=bool(np.array_equal(last,pred))
  rr=dict(call=call,row=row,meter=dict(flops=int(ctx.flops_used),wall_time_s=float(ctx.wall_time_s),residual_wall_time_s=float(ctx.residual_wall_time_s),outer_wall_time_s=wall),checks=checks,peak_rss_bytes=rss,setup_s=setup,prediction_sha256=arrayhash(pred))
  np.savez_compressed(out/f'PREDICTION-{call:02d}-{row}.npz',prediction=pred);write(f'CALL-{call:02d}.json',rr);records.append(rr);print(json.dumps(rr),flush=True);last=pred;del mlp
  if not all(checks.values()):break
 qualification=dict(algorithm_id=alg,probe=freeze['probe'],archive_path=str(archive.relative_to(R)),archive_sha256=sha(archive),source_hashes=freeze['source_hashes'],records=records,imports=sorted(set(imports)),manifest_pass=True,clean_archive_pass=True,fallback_pass=True,pass_=len(records)==len(freeze['archive_new_rows']) and all(all(x['checks'].values()) for x in records),runtime='FlopScope0.12.3/WhestBench0.16.2/Python3.12.3',targets_accessed=False,utc=datetime.now(timezone.utc).isoformat())
 write('QUALIFICATION.json',qualification)
 print(json.dumps({k:v for k,v in qualification.items() if k not in ['records','source_hashes','imports']}),flush=True)
