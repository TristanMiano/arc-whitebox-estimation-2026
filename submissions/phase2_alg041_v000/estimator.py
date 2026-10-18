"""ALG041-V000: full-history CSK3-R with fixed JSP fresh-source response."""
import flopscope as flops
import flopscope.numpy as fnp
from whestbench import BaseEstimator
from fast_kernel import RectangularMultiplier
from moments import propagate, uni
from joint_source import joint_off_diagonal
class Estimator(BaseEstimator):
    def setup(self,ctx):
        n=ctx.width;self.multiplier=RectangularMultiplier(n)
        for blocks in range(1,5):
            self.multiplier.prepare(blocks*n,n,n)
            self.multiplier.prepare(n,2*blocks*n,n)
    def predict(self,mlp,budget):
        n=mlp.width
        mm=getattr(self,'multiplier',None)
        if mm is None or mm.n!=n:mm=RectangularMultiplier(n)
        mu=fnp.zeros(n,dtype=fnp.float64);C=fnp.eye(n,dtype=fnp.float32)
        a=fnp.zeros(n,dtype=fnp.float64);D=fnp.zeros((n,n),dtype=fnp.float32)
        A=fnp.empty((n,0),dtype=fnp.float32);B=fnp.empty((n,0),dtype=fnp.float32)
        E=fnp.zeros((n,n),dtype=fnp.float32);h=0.;scale=1.;rows=[]
        for layer,w in enumerate(mlp.weights):
            M=w.T
            mup=M@mu;ap=M@a
            if layer==len(mlp.weights)-1:
                gd=fnp.sum(M*M,axis=1,dtype=fnp.float64)
                v=gd if layer==0 else fnp.sum(mm.multiply(M,C)*M,axis=1,dtype=fnp.float64)
                dv=fnp.diag(D).astype(fnp.float64) if layer==0 else fnp.sum(mm.multiply(M,D)*M,axis=1,dtype=fnp.float64)
                At=mm.transform(M,A);Bt=mm.transform(M,B)
                k=fnp.sum(At*Bt*Bt,axis=1,dtype=fnp.float64)
                if layer:
                    V=mm.multiply(M,E)
                    k=k+fnp.sum(V*M*M,axis=1,dtype=fnp.float64)
                l=3*h*gd*gd/(n*(n+2))
                u=uni(mup,fnp.maximum(v,1e-30),ap,dv,k,l)
                rows.append((fnp.maximum(u['m']+u['dm'],0)*scale).astype(fnp.float32))
                break
            G=fnp.einsum('ik,jk->ij',M,M)
            Cp=G if layer==0 else mm.multiply(mm.multiply(M,C),w)
            Dp=mm.multiply(mm.multiply(M,D),w) if layer else D
            At=mm.transform(M,A);Bt=mm.transform(M,B)
            Scp=mm.slice(At,Bt)
            V=mm.multiply(M,E) if layer else E
            Sr=mm.multiply(fnp.concatenate((2*V*M,M*M),axis=1),fnp.concatenate((M.T,V.T),axis=0))/3 if layer else E
            Sp=(Scp+Sr).astype(fnp.float64)
            result=propagate(mup,Cp.astype(fnp.float64),ap,Dp.astype(fnp.float64),Sp,G.astype(fnp.float64),h)
            mu,C64,a,D64,S,h,d,e,k=result
            rows.append((fnp.maximum(mu+a,0)*scale).astype(fnp.float32))
            oldA=d[:,None]*At;oldB=d[:,None]*Bt
            Sold=d[:,None]**2*d*Scp
            F=joint_off_diagonal(mup,Cp,ap,Dp,Sp,d,e) if layer else d[:,None]*Cp
            fnp.fill_diagonal(F,0.)
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
