"""Rebuild submission writeups and time tables from the frozen public evidence."""
from pathlib import Path
from datetime import datetime
import csv,json,re
R=Path(__file__).resolve().parents[1]
read=lambda p:json.loads((R/p).read_text())
entries=read('evidence/submissions.json');tasks=read('evidence/task_times.json')
failed=read('evidence/failed_attempts.json')
def write(path,text):
 p=R/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def dump(path,data):write(path,json.dumps(data,indent=2,allow_nan=False)+'\n')
def dt(s):return datetime.fromisoformat(s.replace('Z','+00:00'))
def link(path,label):return f'[{label}](../{path})'
groups=[];last=-1;cum=0
for event in sorted({e['event'] for e in entries}):
 es=[e for e in entries if e['event']==event]
 ts=[t for t in tasks if last<t['sequence']<=event]
 mins=sum(t['session_minutes'] or 0 for t in ts);cum+=mins
 group=dict(event=event,task_id=es[0]['task_id'],submission_ids=[e['submission_id'] for e in es],
  task_ids=[t['task_id'] for t in ts],task_count=len(ts),recorded_session_minutes=mins,
  active_research_minutes=sum(t.get('active_research_minutes') or 0 for t in ts),
  mathematics_minutes=sum(t.get('active_mathematics_minutes') or 0 for t in ts),
  agent_person_minutes=sum(t.get('agent_person_minutes') or 0 for t in ts),
  missing_task_times=[t['task_id'] for t in ts if t['session_minutes'] is None],
  cumulative_session_minutes=cum)
 groups.append(group);last=event
accounted=[t for t in tasks if t['sequence']<=last]
assert abs(cum-sum(t['session_minutes'] or 0 for t in accounted))<1e-7
assert len({tid for g in groups for tid in g['task_ids']})==len(accounted)
summary=dict(successful_algorithm_versions=len(entries),failed_attempts=len(failed),
 recorded_tasks_through_last_submission=len(accounted),
 timed_tasks=sum(t['session_minutes'] is not None for t in accounted),
 missing_task_times=sum(t['session_minutes'] is None for t in accounted),
 recorded_session_hours=cum/60,
 active_research_or_work_hours=sum(t.get('active_research_minutes') or 0 for t in accounted)/60,
 recorded_mathematics_hours=sum(t.get('active_mathematics_minutes') or 0 for t in accounted)/60,
 overlapping_agent_person_hours=sum(t.get('agent_person_minutes') or 0 for t in accounted)/60,
 post_submission_documentation_minutes=sum(t['session_minutes'] or 0 for t in tasks if t['sequence']>last),
 caveat='Recorded task sessions, not human hours or model token-thinking time. T172 active_work includes engineering/records. Untimed work and this release task are excluded.')
dump('evidence/time_groups.json',groups);dump('evidence/time_summary.json',summary)
with (R/'evidence/task_times.csv').open('w',newline='') as f:
 keys=list(dict.fromkeys(k for row in tasks for k in row));w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(tasks)
with (R/'evidence/submissions.csv').open('w',newline='') as f:
 keys=['algorithm_id','submission_id','task_id','adjusted_score','raw_mse','archive_sha256','archive','writeup'];w=csv.DictWriter(f,fieldnames=keys,extrasaction='ignore');w.writeheader();w.writerows(entries)

lines=['# Submission chronology and recorded effort','',
 f'Through the last submission task, **{summary["recorded_session_hours"]:.2f} recorded task-session hours** cover **{len(accounted)} started tasks**. '
 f'Of those tasks, **{summary["missing_task_times"]} have no recorded duration**; two older records are partial. '
 f'The record includes **{summary["active_research_or_work_hours"]:.2f} hours explicitly labeled active research/work**, '
 f'of which **{summary["recorded_mathematics_hours"]:.2f} hours were separately labeled mathematics/theory**. '
 'These are overlapping subsets, not additional time. T172 uses a broader active-work category than earlier rounds.','',
 'The table sums recorded sessions since the previous successful submission task, including intervening failed ideas, protocol work, literature, experiments, engineering and grader waits. '
 'It uses task-completion boundaries rather than subtracting calendar submission dates. It does not attribute all intervening work causally to the winning mechanism. '
 'Two T075 submissions and three T172 submissions share their task-group total; a repeated “shared” cell is never an extra amount.','',
 '| Task | Algorithm / submission | Official adjusted score | Recorded hours since prior group | Active research/work hours | Tasks in group | Cumulative recorded hours |',
 '|---|---|---:|---:|---:|---:|---:|']
for g in groups:
 for i,e in enumerate(x for x in entries if x['event']==g['event']):
  hours=f'{g["recorded_session_minutes"]/60:.2f}' if i==0 else 'shared above'
  active=f'{g["active_research_minutes"]/60:.2f}' if i==0 and g['active_research_minutes'] else '—'
  lines.append(f'| {e["task_id"]} | [{e["algorithm_id"]} / {e["submission_id"]}](../{e["writeup"]}) | {e["adjusted_score"]:.11g} | {hours} | {active} | {g["task_count"] if i==0 else "shared"} | {g["cumulative_session_minutes"]/60:.2f} |')
lines+=['','## Within the final research task','',
 'T172 has sufficiently detailed intervals to subdivide its shared total. Boundaries below use the first saved observation of each successful grade; the final interval includes task closeout. These intervals partition T172 and must not be added to its table total. They measure task sessions, including concurrent numerical execution/monitoring, not isolated model reasoning.','',
 '| Endpoint | Session minutes in interval | Explicit active-work minutes in interval |','|---|---:|---:|']
timing=read('experiments/theory/t172/TIMING.json');segments=read('experiments/theory/t172/TIMING_SEGMENTS.json')['closed'];start=dt(timing['start_utc'])
splits=[]
for i,e in enumerate(x for x in entries if x['task_id']=='T172'):
 j=read(e['source']);end=dt(j['observed_utc']) if i<2 else dt(timing['record_completion_utc'])
 active=0
 for s in segments:
  if s['category']=='passive':continue
  active+=max(0,(min(end,dt(s['end_utc']))-max(start,dt(s['start_utc']))).total_seconds())/60
 mins=(end-start).total_seconds()/60
 splits.append(dict(submission_id=e['submission_id'],start_utc=start.isoformat(),end_utc=end.isoformat(),session_minutes=mins,active_work_minutes=active))
 lines.append(f'| {e["submission_id"]}'+(' + closeout' if i==2 else '')+f' | {mins:.2f} | {active:.2f} |');start=end
assert abs(sum(s['session_minutes'] for s in splits)-timing['elapsed_minutes'])<1e-6
assert abs(sum(s['active_work_minutes'] for s in splits)-timing['active_work_minutes'])<1e-6
dump('evidence/t172_submission_intervals.json',splits)
lines+=['','## Failed attempts and accounting limits','',
 '| Attempt | Algorithm | Outcome |','|---:|---|---|']
for f in failed:lines.append(f'| {f["submission_id"]} | {f["algorithm_id"]} | {f["reason"]} |')
lines+=['',
 'Both failures are included within their task-session totals. The records do not support a separate research-hour attribution to each failed/repaired upload. '
 'There are 26 recorded attempts for these 24 graded versions. The early Phase-1-oriented exploration did not record an official submission. This inventory is reconstructed from saved receipts and reports, not an independent export of all server account activity.','',
 '- The earlier T159A audit supplies the first 151 task records (100.70 recorded hours). Its prior pause adjustments are retained. Its own 12.42-minute audit enters the later T161 interval.',
 '- T162’s explicitly recorded 441.49-minute interruption is excluded. For T169 and T170, the entire mixed passive/interruption buckets (56.39 and 709.92 minutes) are conservatively excluded. Raw elapsed values and deductions remain in the CSV.',
 '- T172 retains its 44.05 minutes of recorded passive evaluator/local waiting within session time, while excluding those minutes from active work. Ordinary task waiting is included where recorded; crash gaps are not interchangeable with that waiting.',
 f'- T129 records {summary["overlapping_agent_person_hours"]:.2f} overlapping sub-agent person-hours, reported separately and never added to root elapsed time.',
 '- Thirty-six tasks are untimed, T026/T120A are partially timed, seven pre-numbered research events have no duration, and the visualization-repair follow-up is untimed. Unrecorded conversations, imported Fable/Opus effort, token usage and human supervision time cannot be recovered.',
 f'- T173’s {summary["post_submission_documentation_minutes"]:.2f} minutes of final-selection/writeup work occur after the final submission and are excluded from milestone totals. Publication preparation is also excluded.',
 '- A recorded hour is agent task-session time. It is not one hour of human labor, paid compute, GPU execution, or model inference telemetry. Categories were maintained by the agent and are approximate.',
 '', '## Rebuild and inspect','',
 'Run `python3 tools/build_reports.py`. Inputs: [task records](../evidence/task_times.json), [submissions](../evidence/submissions.json), and preserved T172 timing. Outputs: [task CSV](../evidence/task_times.csv), [submission CSV](../evidence/submissions.csv), [groups](../evidence/time_groups.json), [summary](../evidence/time_summary.json). '
 'The earlier [T159A audit](SUBMISSION_MILESTONE_TIME_AUDIT.md) remains dated historical context; this table extends it.','']
write('docs/SUBMISSION_TIMELINE.md','\n'.join(lines))

index=['# Submitted algorithms','',
 'Each page below describes one successfully graded version, its inherited machinery and project changes, official result, retained package and limits of the evidence. '
 'These are retrospective technical notes. Only the final 336809 report is the formal challenge writeup draft. '
 '“Local” includes AI-assisted project work; no academic priority is implied.','',
 '| Algorithm | Submission | Adjusted score | Provenance / type of change |','|---|---:|---:|---|']
for e in entries:
 a=e['algorithm_id'];p=e['provenance'];g=next(g for g in groups if g['event']==e['event']);record=read(e['source']);sd=R/e['source_directory']
 technical=(sd/'README.md').read_text() if (sd/'README.md').is_file() else ''
 # Preserve shipping description verbatim; quote as historical text to avoid
 # treating its stale instructions/relative links as a new reproducibility claim.
 note='\n'.join('> '+x for x in technical.splitlines())
 extra=''
 for key in ['variant_change','semantic_delta','mechanism_family']:
  spec=read(f'state/algorithm_specs/{a}.json')
  if key in spec and isinstance(spec[key],str):extra+=f'\n{spec[key]}\n'
 observations=[]
 for key in ['local_mean_adjusted_ratio','local_mean_raw_ratio','local_adjusted_wins','local_networks','bootstrap_support','new_fits','new_full_shape_calls']:
  if key in record: observations.append(f'- `{key}`: {record[key]}')
 failures=[f for f in failed if f['algorithm_id']==a]
 raw=f'{e["raw_mse"]:.13g}' if e['raw_mse'] is not None else 'See original task receipt'
 text=f'''# {a}: {p['short_label']}

**Successfully graded submission {e['submission_id']}**, task {e['task_id']}.
Official public adjusted score: **{e['adjusted_score']:.13g}**; raw final-layer MSE: **{raw}**.
These are saved public grades, not private final ranks. Historical scores can involve different evaluator versions.

## Method and contribution

{p['local_change']}
{extra}
All entries solve the same Phase 2 problem: predict the layerwise expected ReLU activations of a known width-1024, depth-16 random MLP under standard-normal input. The objective is the mean of per-network final-layer MSE multiplied by `max(0.1, FLOPs / 2**41)`. A lower raw error can still be a worse adjusted score if compute grows too much.

## Technical description retained with the source

The following is the package's historical description. Embedded paths/commands refer to its original research workspace; use the current reproduction guide below for this public release.

{note}

## Evidence and limitations

The official result is supported by the {link(e['source'],'preserved receipt/result')}. The {link(f'state/algorithm_specs/{a}.json','algorithm specification')} records the implementation and evaluation scope. The source description and recorded deltas above explain what was inherited and what changed; they are not a proof of academic novelty.

{chr(10).join(observations) or 'See the task record for local comparison and qualification details; this release performs no new benchmark.'}

Repeatedly exposed development networks and fitted public-training data are not fresh private validation. Bootstrap support, where reported, is descriptive and is not a calibrated posterior probability. An official grade confirms that attempt produced a score; it does not establish the proposed mechanism, future private rank, or final prize eligibility.

## Source and reproduction

- {link(e['source_directory']+'/estimator.py','Exact archived estimator source')}
- {link(e['archive'],'Preserved accepted package')}, SHA-256 `{e['archive_sha256']}`
- Archived runtime metadata: `{json.dumps(e['runtime'],sort_keys=True)}`. Null fields mean the old manifest did not record that version; do not infer a version from newer entries.
- {link('docs/REPRODUCTION.md','Reproduction instructions')} and {link('THIRD_PARTY_NOTICES.md','licenses / attribution')}

The package contains its required static assets. Extract it unchanged when reproducing the accepted version. Later public-release license notices supplement early packages without altering the archived bytes. API/data/runtime changes can change historical numerical results and costs.

## Effort and development history

The task group ending at {e['task_id']} contains **{g['recorded_session_minutes']/60:.2f} recorded session hours** over {g['task_count']} tasks since the preceding successful submission group, reaching **{g['cumulative_session_minutes']/60:.2f} cumulative recorded hours**. {('This total is shared by multiple submissions in the same task; do not count it once per algorithm.' if len(g['submission_ids'])>1 else '')} It includes failed ideas and operational work and does not measure this algorithm's isolated invention time. See the {link('docs/SUBMISSION_TIMELINE.md','complete chronology')} and {link('docs/WORKFLOW_AND_MODEL_REPORT.md','agent/workflow report')}.
'''
 if failures:text+='\n## Earlier failed attempt\n\n'+'\n'.join(f'- {f["submission_id"]}: {f["reason"]}' for f in failures)+'\n'
 if a=='ALG058-V001':text+='\n## Full technical report\n\nSee the [12-page final PDF](../experiments/finalization/t174/writeup/arc-whestbench-phase2-336809.pdf) and [editable LaTeX](../experiments/finalization/t174/writeup/main.tex). The report corresponds to submission 336809 only. GitHub publication is separate from forum delivery; see the repository README for delivery status.\n'
 write(e['writeup'],text)
 index.append(f'| [{a}]({a}.md) | {e["submission_id"]} | {e["adjusted_score"]:.11g} | {p["short_label"]} |')
index+=['','The failed attempts are documented on the ALG018 and ALG024 pages and in the [chronology](../docs/SUBMISSION_TIMELINE.md). Locally rejected candidates were not submitted; their reports remain in the historical research evidence.','']
write('writeups/README.md','\n'.join(index))
print(json.dumps(summary,indent=2))
