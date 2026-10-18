"""Verify public release/accepted archive identity without executing estimators."""
from pathlib import Path
import ast,hashlib,json,tarfile
R=Path(__file__).resolve().parents[1]
digest=lambda data:hashlib.sha256(data).hexdigest()
manifest=json.loads((R/'RELEASE_MANIFEST.json').read_text())
for name,h in manifest['files'].items():
    assert digest((R/name).read_bytes())==h,('release mismatch',name)
entries=json.loads((R/'evidence/submissions.json').read_text())
assert len(entries)==24 and len({x['submission_id'] for x in entries})==24
for e in entries:
    archive=R/e['archive'];assert digest(archive.read_bytes())==e['archive_sha256']
    with tarfile.open(archive) as t:
        members=t.getmembers()
        assert all(m.isfile() and not Path(m.name).is_absolute() and '..' not in Path(m.name).parts for m in members)
        m=json.loads(t.extractfile('manifest.json').read())
        for f in m['files']:
            data=t.extractfile(f['name']).read()
            assert digest(data)==f['sha256'],(e['algorithm_id'],f['name'])
            assert (R/e['source_directory']/f['name']).read_bytes()==data
            if f['name'].endswith('.py'):ast.parse(data)
    assert (R/e['writeup']).is_file()
print(json.dumps(dict(release_files=len(manifest['files']),accepted_versions=len(entries),archive_and_source_identity=True,estimator_executions=0),indent=2))
