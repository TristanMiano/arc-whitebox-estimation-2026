"""Fixed H143-JSP fresh B leg; all inputs are pre-activation moments."""
import flopscope.numpy as fnp

def joint_off_diagonal(m,C,a,D,S,d,e):
    v=fnp.maximum(fnp.diag(C).astype(fnp.float64),1e-30)
    diagD=fnp.diag(D).astype(fnp.float64)
    r=-m/v
    delta_d=e*a+0.5*r*e*diagD
    theta=r*a+0.5*(m*m/v-1)/v*diagD
    F=d[:,None]*C
    F=F*(1+0.5*theta[None,:])
    F=F+(0.5*e[:,None]*C)*(r[None,:]*C)
    F=F+0.5*e[:,None]*S+0.5*d[:,None]*(r[None,:]*S.T)
    F=F+delta_d[:,None]*C+d[:,None]*D
    fnp.fill_diagonal(F,0.)
    return F
