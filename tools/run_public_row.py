"""Meter one archived estimator on a locally supplied public-data NPZ row."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, os, re, sys, time

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--row',type=Path,required=True,help='Public row NPZ with weights and scalar mlp_seed; never a private evaluation row.')
    p.add_argument('--submission',type=Path,default=Path('submissions/phase2_alg058_v001'))
    p.add_argument('--output',type=Path,default=Path('runs/public-row'))
    args=p.parse_args()
    import numpy as np
    import flopscope as flops
    from whestbench import MLP,SetupContext
    source=args.submission.resolve(); f=source/'estimator.py'
    assert f.is_file(),f
    with np.load(args.row,allow_pickle=False) as z:
        weights=np.asarray(z['weights']);seed=int(np.asarray(z['mlp_seed']).item())
    assert weights.shape==(16,1024,1024),weights.shape
    assert np.isfinite(weights).all()
    # Input loading/contract checking belong to the harness, not estimator work.
    mlp=MLP.from_row({'weights':weights,'mlp_seed':seed},seed_protocol_version='2.0')
    code=f.read_text()
    for key in set(re.findall(r'(?:_os|os)\.environ\.get\([\"\']([^\"\']+)',code)):
        os.environ.pop(key,None)
    sys.path.insert(0,str(source))
    spec=importlib.util.spec_from_file_location('estimator',f)
    module=importlib.util.module_from_spec(spec);sys.modules['estimator']=module;spec.loader.exec_module(module)
    estimator=module.Estimator();start=time.perf_counter()
    estimator.setup(SetupContext(width=1024,depth=16,flop_budget=2**41,api_version='2.0',submission_dir=str(source),seed=0))
    setup_s=time.perf_counter()-start
    with flops.BudgetContext(flop_budget=2**41,wall_time_limit_s=120,quiet=True) as ctx:
        prediction=estimator.predict(mlp,2**41)
    prediction=np.asarray(prediction,dtype=np.float32)
    assert prediction.shape==(16,1024) and np.isfinite(prediction).all()
    args.output.mkdir(parents=True,exist_ok=False)
    np.savez_compressed(args.output/'prediction.npz',prediction=prediction)
    result=dict(source_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),setup_s=setup_s,
        flops=int(ctx.flops_used),wall_time_s=float(ctx.wall_time_s),residual_wall_time_s=float(ctx.residual_wall_time_s),
        scope='One public input; no labels, accuracy estimate, replay qualification or official submission.',
        prediction_shape=list(prediction.shape))
    (args.output/'meter.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
