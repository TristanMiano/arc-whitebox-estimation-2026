"""Build the final PDF from the saved LaTeX project; no model or data execution."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

B=Path(__file__).resolve().parent
R=B.parents[2]
binary=shutil.which('tectonic') or str(R/'tmp/t173-tools/tectonic')
with (B/'BUILD.log').open('w') as out:
    subprocess.run([binary,'main.tex','--keep-logs','--keep-intermediates'],cwd=B/'writeup',stdout=out,stderr=subprocess.STDOUT,check=True)
dest=B/'writeup/arc-whestbench-phase2-336809.pdf'
shutil.copyfile(B/'writeup/main.pdf',dest)
manifest={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [B/'writeup/main.tex',B/'writeup/appendix.tex',B/'writeup/images/method.pdf',B/'writeup/images/paired12.pdf',dest]}
(B/'DOCUMENT_HASHES.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(dest)
