"""P82/ALG058-V001: exact normalization-preserving batch of the two sources."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,ast,numpy as np
B=Path(__file__).resolve().parent;name='P82_anchor_merged';p=B/'sources'/name;shutil.copytree(B/'sources/P75_context64data',p)
a=json.loads((p/'nn_asset.json').read_text());b=json.loads((B/'sources/P19_new_trace/nn_asset.json').read_text());h=np.zeros((64,72));h[:32,:48]=a['hw'];h[32:,48:]=b['hw'];z=dict(mean=a['mean']+b['mean'],scale=a['scale']+b['scale'],hw=h.tolist(),hb=a['hb']+b['hb'],ow=np.concatenate([.5*np.array(a['ow']),.5*np.array(b['ow'])],axis=1).tolist(),ob=(.5*np.array(a['ob'])+.5*np.array(b['ob'])).tolist())
# Different old/new normalizers remain separate coordinates before clipping.
rng=np.random.default_rng(172082);x=(np.asarray(a['mean'])+np.asarray(a['scale'])*rng.normal(size=(257,48))*10).astype(np.float32);xx=np.concatenate([x,x[:,:24]],axis=1)
def pred(asset,v):
 ar=lambda k:np.asarray(asset[k],dtype=np.float32)
 return np.tanh(np.clip((v-ar('mean'))/ar('scale'),-8,8)@ar('hw').T+ar('hb'))@ar('ow').T+ar('ob')
err=float(np.max(abs(pred(z,xx)-.5*(pred(a,x)+pred(b,x[:,:24])))));assert err<2e-5
(p/'nn_asset.json').write_text(json.dumps(z)+'\n');s=(p/'estimator.py').read_text();needle='                features=fnp.concatenate([features,fnp.broadcast_to(fnp.mean(features,axis=0),features.shape)],axis=1)';assert s.count(needle)==1;s=s.replace(needle,needle+'\n                features=fnp.concatenate([features,features[:,:24]],axis=1)');ast.parse(s);(p/'estimator.py').write_text(s)
cfg=dict(probe=name,question='Can a single batched source evaluation restore residual-time margin for the unchanged equal mean-source average?',source_sha256=hashlib.sha256(s.encode()).hexdigest(),asset_sha256=hashlib.sha256((p/'nn_asset.json').read_bytes()).hexdigest(),training_networks=64,secondary_training_networks=32,paired_source=dict(primary='P75 context48 trained64',secondary='ALG055/P19 trace24 trained32',weights=[.5,.5]),merged_normalizers=True,float32_merge_max_abs=err,origin='P19 physical path; fixed equal source average with72 normalized coordinates and64 hidden units. Duplicated local coordinates preserve the different normalizers and clipping exactly before rounding.',created_utc=datetime.now(timezone.utc).isoformat(),rows=[750,976,772,795],data_role='Adaptive exposed development; no new fitting. ALG058-V000 residual-cap miss preserved separately.')
(p/'CONFIG.json').write_text(json.dumps(cfg,indent=2)+'\n');(B/'P82_MERGE_IDENTITY.json').write_text(json.dumps(dict(float32_max_abs=err,pass_=True,scope='All four output heads on257 synthetic feature vectors spanning clipped and unclipped regions; separate versus batched normalizers.'),indent=2)+'\n')
with (B/'PROBES.jsonl').open('a') as f:f.write(json.dumps(cfg)+'\n')
print(json.dumps(cfg))
