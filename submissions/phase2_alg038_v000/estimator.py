"""ALG038-V000: unfit CSK3-R joint-cumulant linear response."""
import flopscope as flops
import flopscope.numpy as fnp
from whestbench import BaseEstimator
from fast_kernel import RectangularMultiplier
from moments import propagate
class Estimator(BaseEstimator):
    def setup(self,ctx):pass
    def predict(self,mlp,budget):
        n=mlp.width;mm=RectangularMultiplier(n)
        mu=fnp.zeros(n,dtype=fnp.float64);C=fnp.eye(n,dtype=fnp.float32)
        a=fnp.zeros(n,dtype=fnp.float64);D=fnp.zeros((n,n),dtype=fnp.float32)
        A=fnp.empty((n,0),dtype=fnp.float32);B=fnp.empty((n,0),dtype=fnp.float32)
        E=fnp.zeros((n,n),dtype=fnp.float32);h=0.;scale=1.;rows=[]
        for layer,w in enumerate(mlp.weights):
            M=w.T
            mup=M@mu;ap=M@a
            G=fnp.einsum('ik,jk->ij',M,M)
            Cp=G if layer==0 else mm.multiply(mm.multiply(M,C),w)
            Dp=mm.multiply(mm.multiply(M,D),w) if layer else D
            At=mm.transform(M,A);Bt=mm.transform(M,B)
            Scp=mm.slice(At,Bt)
            V=mm.multiply(M,E) if layer else E
            Sr=mm.multiply(fnp.concatenate((2*V*M,M*M),axis=1),fnp.concatenate((M.T,V.T),axis=0))/3 if layer else E
            Sp=(Scp+Sr).astype(fnp.float64)
            result=propagate(mup,Cp.astype(fnp.float64),ap,Dp.astype(fnp.float64),Sp,G.astype(fnp.float64),h,final=layer==len(mlp.weights)-1)
            if layer==len(mlp.weights)-1:
                m,da=result;rows.append((fnp.maximum(m+da,0)*scale).astype(fnp.float32));break
            mu,C64,a,D64,S,h,d,e,k=result
            rows.append((fnp.maximum(mu+a,0)*scale).astype(fnp.float32))
            oldA=d[:,None]*At;oldB=d[:,None]*Bt
            Sold=d[:,None]**2*d*Scp
            F=d[:,None]*Cp;fnp.fill_diagonal(F,0.)
            q=fnp.sqrt(fnp.maximum(k,0)/(3*fnp.maximum(e,1e-300)))
            q=fnp.where(e>1e-280,q,0.)
            Ssource=e*(F*F)+2*(e*q)[:,None]*F.T
            fnp.fill_diagonal(Ssource,k)
            sourceA=fnp.diag(3*e);sourceB=F+fnp.diag(q)
            A=fnp.concatenate((oldA,sourceA),axis=1)
            B=fnp.concatenate((oldB,sourceB),axis=1)
            R=S-Sold-Ssource;E=3*R.T;fnp.fill_diagonal(E,fnp.diag(R))
            s=fnp.sqrt(fnp.maximum(fnp.max(fnp.diag(C64)),1e-30))
            mu=mu/s;a=a/s;C=(C64/(s*s)).astype(fnp.float32);D=(D64/(s*s)).astype(fnp.float32)
            A=(A/s).astype(fnp.float32);B=(B/s).astype(fnp.float32);E=(E/(s*s*s)).astype(fnp.float32)
            h=h/(s**4);scale=scale*s
        return fnp.stack(rows,axis=0)
