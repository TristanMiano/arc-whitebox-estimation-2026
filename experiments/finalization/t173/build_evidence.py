"""Summarize preserved evidence for the writeup; no estimator execution or fitting."""
from pathlib import Path
import ast
import hashlib
import json
import numpy as np

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
T172 = ROOT / 'experiments/theory/t172'

def read(path):
    return json.loads(path.read_text())

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

official = read(BASE / 'CURRENT_GRADES.json')
summary = {'official_grades': official, 'scope': 'Reanalysis of existing evidence; no new inference, training or private evaluation.'}
summary['candidates'] = {}
for alg in ['ALG054-V000', 'ALG055-V000', 'ALG058-V001']:
    p = T172 / 'candidates' / alg
    score, qual = read(p / 'SCORE.json'), read(p / 'QUALIFICATION.json')
    probe = qual['probe']
    pilot = read(T172 / 'runs' / probe / 'RESULT.json')
    calls = pilot['records'] + qual['records']
    records = score['records']
    summary['candidates'][alg] = {
        'n': len(records), 'mean_raw': score['mean_raw'], 'mean_adjusted': score['mean_adjusted'],
        'mean_flops': float(np.mean([r['flops'] for r in records])),
        'flops_range': [min(r['flops'] for r in records), max(r['flops'] for r in records)],
        'max_residual_s': max(r['meter']['residual_wall_time_s'] for r in calls),
        'max_wall_s': max(r['meter']['wall_time_s'] for r in calls),
        'max_setup_s': max(r['setup_s'] for r in calls),
        'peak_rss_bytes': max(r['peak_rss_bytes'] for r in calls),
        'all_checks_pass': all(all(r['checks'].values()) for r in calls),
        'qualification_pass': qual['pass_'],
        'rows': [r['row'] for r in records], 'adjusted_by_row': [r['adjusted'] for r in records],
        'source': str((p/'SCORE.json').relative_to(ROOT)), 'source_sha256': digest(p/'SCORE.json'),
    }

summary['matched_four'] = {}
for probe in ['P02_e30', 'P09_fused_cov', 'P19_new_trace', 'P82_anchor_merged']:
    path = T172 / 'runs' / probe / 'RESULT.json'
    d = read(path)
    summary['matched_four'][probe] = {
        'mean_raw': d['mean_raw'], 'mean_adjusted': d['mean_adjusted'],
        'mean_flops': float(np.mean([r['meter']['flops'] for r in d['records']])),
        'rows': [r['row'] for r in d['records']],
        'source': str(path.relative_to(ROOT)), 'source_sha256': digest(path),
    }
assert len({tuple(v['rows']) for v in summary['matched_four'].values()}) == 1
base = summary['matched_four']['P02_e30']
for d in summary['matched_four'].values():
    d['adjusted_ratio_to_public'] = d['mean_adjusted']/base['mean_adjusted']
    d['raw_ratio_to_public'] = d['mean_raw']/base['mean_raw']

src = (ROOT/'submissions/phase2_alg058_v001/estimator.py').read_text()
constants = {}
for node in ast.parse(src).body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ['COVARIANCE_COEFFICIENTS','EXTRA_COEFFICIENTS','MIXED_COEFFICIENTS','QUADRATIC_COEFFICIENTS']:
                constants[target.id] = ast.literal_eval(node.value)
fit = read(ROOT/'experiments/theory/t170/P27_FIT/RESULT.json')
coef = fit['results']['local_and_terminal']['whole_training_coefficients']
flattened = [x for key in ['COVARIANCE_COEFFICIENTS','EXTRA_COEFFICIENTS','MIXED_COEFFICIENTS','QUADRATIC_COEFFICIENTS'] for block in constants[key] for x in block]
assert len(flattened) == 96 and flattened == coef
summary['covariance_asset'] = {'coefficient_count':96,'training_rows':fit['rows'],'equals_T170_all32_fit':True,'lambda':fit['lambda_'],'fit_source':'experiments/theory/t170/P27_FIT/RESULT.json','constants':constants}

trace = read(T172/'P14_FIT/trace24-ALL-asset.json')
context = read(T172/'P65_EXPANDED_FIT/context48-ALL-asset.json')
merged = read(ROOT/'submissions/phase2_alg058_v001/nn_asset.json')
for key in ['mean','scale','hb']:
    assert merged[key] == context[key] + trace[key]
H = np.asarray(merged['hw']); expected=np.zeros((64,72))
expected[:32,:48]=context['hw'];expected[32:,48:]=trace['hw']
assert np.array_equal(H,expected)
assert np.array_equal(np.asarray(merged['ow']),np.concatenate([np.asarray(context['ow'])/2,np.asarray(trace['ow'])/2],axis=1))
assert np.array_equal(np.asarray(merged['ob']),(np.asarray(context['ob'])+np.asarray(trace['ob']))/2)
summary['mean_asset'] = {'trace_asset_sha256':digest(T172/'P14_FIT/trace24-ALL-asset.json'),'context_asset_sha256':digest(T172/'P65_EXPANDED_FIT/context48-ALL-asset.json'),'merged_asset_sha256':digest(ROOT/'submissions/phase2_alg058_v001/nn_asset.json'),'exact_block_and_normalizer_identity':True,'trace_training_rows':read(T172/'P14_FIT/trace24-ALL.json')['training_rows'],'context_training_rows':read(T172/'P65_EXPANDED_FIT/context48-ALL.json')['training_rows'],'trace_learned_parameters':932,'context_learned_parameters':1700,'combined_learned_parameters':2632,'note':'72 inputs/64 hidden units are a batch of two independently normalized models, not one jointly trained model.'}
assert summary['mean_asset']['trace_training_rows']==fit['rows']
assert set(summary['mean_asset']['context_training_rows']).isdisjoint(summary['candidates']['ALG058-V001']['rows'])
assert all(v['qualification_pass'] and v['all_checks_pass'] for v in summary['candidates'].values())

(BASE/'WRITEUP_EVIDENCE.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:summary[k] for k in ['matched_four','mean_asset']},indent=2))
