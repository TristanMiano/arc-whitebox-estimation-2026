"""Static research figures from preserved evidence, with no new estimator runs."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

B=Path(__file__).resolve().parent
O=B/'writeup/images';O.mkdir(exist_ok=True)
D=json.loads((B/'WRITEUP_EVIDENCE.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'pdf.fonttype':42,'axes.spines.top':False,'axes.spines.right':False})
navy='#17334d';teal='#167d8d';ochre='#b97921';gray='#53616d'

fig,ax=plt.subplots(figsize=(7.3,3.6));ax.set(xlim=(0,10),ylim=(0,5));ax.axis('off')
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.10,rounding_size=0.08',facecolor=color,edgecolor='none'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color='white',fontsize=10,linespacing=1.45)
def arrow(a,b,color=gray):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,color=color,linewidth=1.5))
box(.2,3.1,2.65,1.2,'Known weights\nGaussian input moments',navy)
box(3.65,3.1,2.65,1.2,'Published engine\nmean / covariance /\nfactored third moments',navy)
box(7.1,3.1,2.65,1.2,'Corrected covariance\ncontinues through\nthe physical recurrence',teal)
arrow((2.95,3.7),(3.55,3.7));arrow((6.4,3.7),(7.,3.7))
ax.text(6.7,4.52,'+ our 32-field source',ha='center',fontsize=9,color=teal)
box(3.65,.65,2.65,1.2,'Local moment features\n24-input + 48-input\nfixed learned sources',ochre)
box(7.1,.65,2.65,1.2,'One shadow mean vector\nGaussian-gate transport\nadd at final output',ochre)
arrow((4.97,3.0),(4.97,1.95));arrow((6.4,1.25),(7.,1.25))
ax.text(.2,.55,'Blue: credited physical engine\nTeal: our covariance adaptation\nOchre: our mean adaptation',color=gray,fontsize=9,linespacing=1.6)
fig.tight_layout(pad=.2)
fig.savefig(O/'method.pdf',bbox_inches='tight');fig.savefig(O/'method.png',dpi=180,bbox_inches='tight');plt.close(fig)

a=np.asarray(D['candidates']['ALG055-V000']['adjusted_by_row']);b=np.asarray(D['candidates']['ALG058-V001']['adjusted_by_row'])
rows=D['candidates']['ALG058-V001']['rows'];pct=100*(b/a-1);order=np.argsort(rows)
fig,ax=plt.subplots(figsize=(7.25,2.55));ax.axhline(0,color=gray,lw=.9)
colors=[teal if p<0 else ochre for p in pct[order]]
ax.bar(np.arange(12),pct[order],color=colors,width=.58)
ax.set_xticks(np.arange(12),np.asarray(rows)[order]);ax.set_xlabel('Exposed development network row')
ax.set_ylabel('Adjusted score change (%)');ax.set_ylim(-1.05,1.05)
ax.text(.02,.95,'ALG058 relative to ALG055; lower is better',transform=ax.transAxes,ha='left',va='top',fontsize=9,color=navy)
ax.grid(axis='y',alpha=.17);ax.set_axisbelow(True);fig.tight_layout()
fig.savefig(O/'paired12.pdf',bbox_inches='tight');fig.savefig(O/'paired12.png',dpi=180,bbox_inches='tight');plt.close(fig)
print('Wrote method and paired-development figures')
