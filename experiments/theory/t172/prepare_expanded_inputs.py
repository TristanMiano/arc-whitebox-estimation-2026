"""P65:32 additional named public F inputs and intermediate labels.
Only selected rows below500 are exposed; no protected blind block is read.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,importlib.util,numpy as np,gc,pyarrow as pa,pyarrow.parquet as pq,hashlib
B=Path(__file__).resolve().parent;R=B.parents[2];old=json.loads((B/'P13_CAPTURE/RESULT.json').read_text())['config']['rows'];rows=[round((i+.5)*500/32) for i in range(32)];rows=[x+1 if x in old else x for x in rows];assert len(set(rows))==32 and not set(rows)&set(old) and min(rows)>=0 and max(rows)<500
sp=importlib.util.spec_from_file_location('prior',R/'experiments/submission_policy/t118a/qualify_exact_package.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
manifest=json.loads((R/'experiments/checkpoint3/t117/FULL_DATASET_MANIFEST.json').read_text());cache=Path('/home/trist/.cache/huggingface/hub/datasets--aicrowd--arc-whestbench-public-2026/blobs');out=R/'tmp/t172-expanded-inputs';out.mkdir(exist_ok=True);records=[];labels=[];checked=set();last=None
for row in rows:
 offset=0
 for sh in manifest['shards']:
  if offset<=row<offset+sh['rows']:break
  offset+=sh['rows']
 p=cache/sh['sha256'];assert p.is_file() and p.stat().st_size==sh['size']
 if sh['sha256'] not in checked:
  h=hashlib.sha256()
  with p.open('rb') as f:
   while z:=f.read(16*1024**2):h.update(z)
  assert h.hexdigest()==sh['sha256'];checked.add(sh['sha256'])
 dst=out/f'row-{row:04d}.npy';rp=out/f'row-{row:04d}.json'
 if rp.exists():rec=json.loads(rp.read_text());assert dst.exists()
 else:
  mlp=m.read_mlp(p,row-offset);w=np.asarray(mlp.weights,dtype=np.float32).copy();np.save(dst,w);rec=dict(row=row,path=str(dst.relative_to(R)),weights_sha256=m.sha256_array(w),mlp_seed=int(mlp.seed),source_sha256=sh['sha256']);rp.write_text(json.dumps(rec)+'\n');del mlp,w
 if last!=sh['sha256']:
  tab=pq.read_table(p,columns=['all_layer_means'],use_threads=False);ar=tab.column(0).chunk(0)
  if hasattr(ar,'storage'):ar=ar.storage
  while isinstance(ar,(pa.ListArray,pa.LargeListArray,pa.FixedSizeListArray)):ar=ar.values
  labelblock=ar.to_numpy(zero_copy_only=False).reshape(tab.num_rows,16,1024).copy();del tab,ar;last=sh['sha256']
 labels.append(labelblock[row-offset].copy());records.append(rec);(B/'P65_INPUT_MANIFEST.json').write_text(json.dumps(dict(rows=rows,source_revision=manifest['revision'],records=records,logical_target_rows=rows,protected_logical_rows_accessed=False),indent=2)+'\n');print(json.dumps(rec),flush=True);gc.collect();pa.default_memory_pool().release_unused()
lp=R/'tmp/t172-expanded-labels.npz';np.savez_compressed(lp,rows=rows,labels=np.asarray(labels));(B/'P65_LABEL_MANIFEST.json').write_text(json.dumps(dict(rows=rows,path=str(lp.relative_to(R)),sha256=hashlib.sha256(lp.read_bytes()).hexdigest(),shape=list(np.asarray(labels).shape),columns=['all_layer_means'],protected_logical_rows_accessed=False),indent=2)+'\n')
