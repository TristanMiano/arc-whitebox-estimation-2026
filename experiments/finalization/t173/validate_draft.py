"""Validate the exported document and evidence links; never execute the estimator."""
from pathlib import Path
import hashlib
import json
import re
import sys

B=Path(__file__).resolve().parent
R=B.parents[2]
sys.path.insert(0,str(R/'tmp/t173-python'))
import pymupdf

p=B/'writeup/arc-whestbench-phase2-336809-draft.pdf'
doc=pymupdf.open(p)
assert len(doc)==12
text='\n'.join(page.get_text() for page in doc)
assert all(s in text for s in ['Tristan Miano','tristan_miano','2.97110640613','1.94467643766'])
assert '??' not in text
compact=re.sub(r'\s+','',text)
for h in ['2c28711f6d44709182886eb6e1535503af415ecd97721b46868b39f2ff0660db','6c295943161d1365afa042948770e451091d6fe16706ee7728505ece62b4ab44','bd824f7c1a7e4d1392e0b8507931e973237eb3ca02cabc9a07b66970d2c8e856']:
    assert h in compact
preview=B/'preview';preview.mkdir(exist_ok=True)
for i,page in enumerate(doc):
    assert 'Draft for author review' in page.get_text()
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            x0,y0,x1,y1=line['bbox']
            assert x0>=35 and x1<=page.rect.width-30 and y0>=15 and y1<=page.rect.height-15,(i+1,line['bbox'])
    page.get_pixmap(matrix=pymupdf.Matrix(1.1,1.1)).save(preview/f'page-{i+1:02d}.png')
log=(B/'BUILD.log').read_text()
assert not any(t in log for t in ['Overfull','undefined references','Undefined control','Missing character'])
for rel,h in json.loads((B/'DOCUMENT_HASHES.json').read_text()).items():
    assert hashlib.sha256((B/rel).read_bytes()).hexdigest()==h
e=json.loads((B/'WRITEUP_EVIDENCE.json').read_text());four=e['matched_four'];off={x['id']:x for x in e['official_grades']}
assert all(x['grading_status_cd']=='graded' for x in e['official_grades'])
assert e['covariance_asset']['equals_T170_all32_fit'] and e['mean_asset']['exact_block_and_normalizer_identity']
checks={'pdf_pages':12,'main_pages':8,'references_pages':1,'appendix_pages':3,'all_pages_author_review_label':True,'no_missing_reference_marker':True,'no_extreme_text_bounds':True,'no_overfull_boxes_or_missing_glyphs':True,'accepted_archive_and_code_hashes_present':True,'own_adjusted_reduction_four':1-four['P82_anchor_merged']['adjusted_ratio_to_public'],'own_compute_increase_four':four['P82_anchor_merged']['mean_flops']/four['P02_e30']['mean_flops']-1,'official_mean_sources_gain':1-off[336809]['score']/off[336778]['score'],'pdf_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'document_identity_check':'All entries in DOCUMENT_HASHES.json match disk','new_estimator_runs':0,'new_training_runs':0,'protected_blind_access':False,'final_nomination_performed':False,'writeup_delivered':False}
(B/'PDF_VALIDATION.json').write_text(json.dumps(checks,indent=2)+'\n')
(B/'PDF_TEXT.txt').write_text(text)
print(json.dumps(checks,indent=2))
