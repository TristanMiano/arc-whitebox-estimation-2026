"""Analytic first-order Gaussian pair response, T136 final moment handoff."""
import flopscope as flops
import flopscope.numpy as fnp
NODES=(.019855071751231912,.10166676129318664,.2372337950418355,.4082826787521751,.591717321247825,.7627662049581645,.8983332387068134,.9801449282487681)
WEIGHTS=(.050614268145188185,.11119051722668709,.15685332293894372,.18134189168918102,.18134189168918102,.15685332293894372,.11119051722668709,.050614268145188185)
def col(x):return x[:,None]
def positive_tail(t,phi):
    p=flops.stats.norm.cdf(-t);ell=phi-t*p
    r2=(t*t+1)*p-t*phi;r3=(t*t+2)*phi-(t**3+3*t)*p
    kt=(t*t-1)*phi+t*(3-t*t)*p+3*ell*r2+6*t*ell*ell+2*ell**3
    lt=t*(3-t*t)*phi+(t**4-6*t*t+3)*p+(12-24*t*t)*ell**2-24*t*ell*r2-4*ell*r3-3*r2*r2-12*ell*ell*r2-24*t*ell**3-6*ell**4
    return kt,lt

def uni(mu,v,a,dv,k,l):
    sigma=fnp.sqrt(v);alpha=mu/sigma
    phi=flops.stats.norm.pdf(alpha);d=flops.stats.norm.cdf(alpha)
    e=phi/sigma;f=-alpha*e/sigma;g=(alpha*alpha-1)*e/v
    m=mu*d+sigma*phi;q=mu*m+v*d;r=mu*q+2*v*m;s=mu*r+3*v*q
    k3=r-3*m*q+2*m*m*m
    k4=s-4*m*r-3*q*q+12*m*m*q-6*m**4
    kt,lt=positive_tail(alpha,phi)
    k3=fnp.where(alpha>0,kt*sigma**3,k3);k4=fnp.where(alpha>0,lt*v*v,k4)
    dm=a*d+.5*dv*e+k*f/6+l*g/24
    dq=2*a*m+dv*d+k*e/3+l*f/12
    dr=3*a*q+3*dv*m+k*d+l*e/4
    ds=4*a*r+6*dv*q+4*k*m+l*d
    dk3=dr-3*m*dq+(6*m*m-3*q)*dm
    dk4=ds-4*m*dr+(12*m*m-6*q)*dq+(-4*r+24*m*q-24*m**3)*dm
    return {'sigma':sigma, 'alpha':alpha, 'phi':phi, 'd':d, 'e':e, 'f':f, 'g':g, 'm':m, 'q':q, 'r':r, 's':s, 'k3':k3, 'k4':k4, 'dm':dm, 'dq':dq, 'dr':dr, 'ds':ds, 'dk3':dk3, 'dk4':dk4}

def propagate(mu,C,a,D,S,G,h,final=False):
    n=mu.shape[0];v=fnp.maximum(fnp.diag(C),1e-30)
    k=fnp.diag(S);z=h/(n*(n+2));gd=fnp.diag(G);l=3*z*gd*gd
    u=uni(mu,v,a,fnp.diag(D),k,l)
    m=u['m'];dm=u['dm']
    if final:return m,dm
    sigma=u['sigma'];alpha=u['alpha'];d=u['d'];e=u['e'];f=u['f'];g=u['g'];q=u['q']
    so=col(sigma)*sigma;rho=fnp.minimum(fnp.maximum(C/so,-.999999),.999999)
    # Diagonals are replaced by exact univariate moments below.
    root=fnp.sqrt(1-rho*rho)
    beta=(alpha-col(alpha)*rho)/root
    pj=flops.stats.norm.cdf(beta);ps=flops.stats.norm.pdf(beta)
    sc=sigma*root;mc=mu-C*col(mu/v)
    bj=mc*pj+sc*ps;qj=mc*bj+sc*sc*pj
    pi=pj.T;bi=bj.T;qi=qj.T
    J=col(e)*ps/sc
    lam=C/col(v)
    P=col(d)*d;cp=fnp.zeros(C.shape,dtype=fnp.float64)
    aa=col(alpha*alpha)+alpha*alpha;ab=col(alpha)*alpha
    for node,weight in zip(NODES,WEIGHTS):
        t=rho*node;den=1-t*t
        density=fnp.exp(-(aa-2*t*ab)/(2*den))/(6.283185307179586*fnp.sqrt(den))
        term=rho*weight*density
        P=P+term;cp=cp+term*(rho-t)
    cp=C*col(d)*d+so*cp
    vp=fnp.maximum(q-m*m,0);fnp.fill_diagonal(cp,vp)
    A=mu*P+sigma*(u['phi']*pi+rho*col(u['phi'])*pj)
    R11=cp+col(m)*m
    R20=col(mu)*A.T+col(v)*P+C*e*bi;R02=R20.T
    R21=col(mu)*R11+col(v)*A+C*A.T;R12=R21.T
    R22=col(mu)*R12+col(v)*R02+2*C*R11
    R22=(R22+R22.T)*.5
    K21=col(mu-2*m)*cp+col(v)*(A-col(d)*m)+C*A.T
    fnp.fill_diagonal(K21,u['k3'])
    K22=R22-col(q)*q-2*col(m)*K21.T-2*m*K21-4*col(m)*m*cp-2*cp*cp
    fnp.fill_diagonal(K22,u['k4'])
    ei=col(e);ej=e;fi=col(f);fj=f;gi=col(g);gj=g;li=lam;lj=lam.T
    U=3*z*col(gd)*G;V=z*(col(gd)*gd+2*G*G)
    coeff=(col(a),a,.5*col(fnp.diag(D)),D,.5*fnp.diag(D),col(k)/6,S/2,S.T/2,k/6,col(l)/24,U/6,V/4,U.T/6,l/24)
    def response(derivs):
        total=fnp.zeros(C.shape,dtype=fnp.float64)
        for c,t in zip(coeff,derivs):total=total+c*t
        return total
    dr11=response((A,A.T,ei*bj,P,ej*bi,fi*bj-ei*li*pj,ei*pj,ej*pi,fj*bi-ej*lj*pi,
        gi*bj-2*fi*li*pj+li*li*J,fi*pj-li*J,J,fj*pi-lj*J,gj*bi-2*fj*lj*pi+lj*lj*J))
    dc=dr11-col(m)*dm-col(dm)*m
    dc=(dc+dc.T)*.5
    dv=u['dq']-2*m*dm;fnp.fill_diagonal(dc,dv)
    dr21=response((2*R11,R20,2*A,2*A.T,ej*qi,2*ei*bj,2*P,2*ej*bi,
        fj*qi-2*ej*lj*bi,2*fi*bj-2*ei*li*pj,2*ei*pj,2*ej*pi,
        2*fj*bi-2*ej*lj*pi,gj*qi-4*fj*lj*bi+2*ej*lj*lj*pi))
    dk21=dr21-col(u['dq'])*m-col(q)*dm-2*col(m)*dc-2*col(dm)*cp
    fnp.fill_diagonal(dk21,u['dk3'])
    dr22=response((2*R12,2*R21,2*R02,4*R11,2*R20,2*ei*qj,4*A,4*A.T,2*ej*qi,
        2*fi*qj-4*ei*li*bj,4*ei*bj,4*P,4*ej*bi,2*fj*qi-4*ej*lj*bi))
    dk22=dr22-col(u['dq'])*q-col(q)*u['dq']-2*col(dm)*K21.T-2*col(m)*dk21.T-2*dm*K21-2*m*dk21-4*(col(dm)*m+col(m)*dm)*cp-4*(col(m)*m+cp)*dc
    fnp.fill_diagonal(dk22,u['dk4'])
    return m,cp,dm,dc,K21+dk21,fnp.sum(K22+dk22),d,e,u['k3']
