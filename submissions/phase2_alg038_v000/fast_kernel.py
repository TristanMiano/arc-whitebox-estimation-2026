"""Shared flat rectangular workspace for the licensed three-level kernel."""
import importlib.util
from pathlib import Path
import flopscope.numpy as fnp
p=Path(__file__).parent/'public_release/public_fast_reference.py'
s=importlib.util.spec_from_file_location('csk3_public_kernel',p)
public=importlib.util.module_from_spec(s);s.loader.exec_module(public)

def _fill_plan(a, b, left_stack, right_stack):
    """Bind public-kernel views without doing arithmetic or reading data."""
    hm, hk, hn = a.shape[-2] // 2, a.shape[-1] // 2, b.shape[-1] // 2
    a11, a12 = a[..., :hm, :hk], a[..., :hm, hk:]
    a21, a22 = a[..., hm:, :hk], a[..., hm:, hk:]
    b11, b12 = b[..., :hk, :hn], b[..., :hk, hn:]
    b21, b22 = b[..., hk:, :hn], b[..., hk:, hn:]
    left, right = left_stack[..., :hm, :hk], right_stack[..., :hk, :hn]
    l = tuple(left[..., i, :, :] for i in range(7))
    r = tuple(right[..., i, :, :] for i in range(7))
    return [
        (fnp.concatenate, ((a22[..., None, :, :], a11[..., None, :, :], a12[..., None, :, :]),), {'axis': -3, 'out': left[..., :3, :, :]}),
        (fnp.concatenate, ((b11[..., None, :, :], b21[..., None, :, :], b22[..., None, :, :]),), {'axis': -3, 'out': right[..., 1:4, :, :]}),
        (fnp.add, (a21, a22), {'out': l[4]}),
        (fnp.subtract, (l[4], a11), {'out': l[5]}),
        (fnp.subtract, (a11, a21), {'out': l[6]}),
        (fnp.subtract, (a12, l[5]), {'out': l[3]}),
        (fnp.subtract, (b12, b11), {'out': r[4]}),
        (fnp.subtract, (b22, r[4]), {'out': r[5]}),
        (fnp.subtract, (b22, b12), {'out': r[6]}),
        (fnp.subtract, (r[5], b21), {'out': r[0]}),
    ]

def _combine_plan(leaves, result):
    hm, hn = result.shape[-2] // 2, result.shape[-1] // 2
    c11, c12 = result[..., :hm, :hn], result[..., :hm, hn:]
    c21, c22 = result[..., hm:, :hn], result[..., hm:, hn:]
    p = tuple(leaves[..., i, :, :] for i in range(7))
    return [(fnp.add, (p[1], p[2]), {'out': c11}),
            (fnp.add, (p[1], p[5]), {'out': c12}),
            (fnp.add, (c12, p[6]), {'out': c21}),
            (fnp.add, (c21, p[4]), {'out': c22}),
            (fnp.add, (c12, p[4]), {'out': c12}),
            (fnp.add, (c12, p[3]), {'out': c12}),
            (fnp.subtract, (c21, p[0]), {'out': c21})]

class RectangularMultiplier:
    def __init__(self,n):
        self.n=n; self.cache={}
        if n%8: self.buffers=None; return
        # Allowed products: at most4n by n, or n by8n, each ending in n.
        maxima=(8*n*n,8*n*n,4*n*n)
        self.buffers=tuple(tuple(fnp.empty((size*7**level//4**level,),dtype=fnp.float32)
            for size in maxima) for level in (1,2,3))
    def multiply(self,a,b):
        m,k=a.shape;n=b.shape[1]
        if self.buffers is None or m%8 or k%8 or n%8 or m>4*self.n or k>8*self.n:return a@b
        shape=(m,k,n)
        if shape not in self.cache:
            work=[]
            for level,(left,right,prod) in enumerate(self.buffers,1):
                batch=(7,)*level; div=2**level
                ls=batch+(m//div,k//div);rs=batch+(k//div,n//div);ps=batch+(m//div,n//div)
                count=7**level
                l=left[:count*m*k//div**2].reshape(ls)
                r=right[:count*k*n//div**2].reshape(rs)
                p=prod[:count*m*n//div**2].reshape(ps)
                work.append((l,r,p))
            (l1,r1,p1),(l2,r2,p2),(l3,r3,p3)=work
            steps=_fill_plan(l1,r1,l2,r2)+_fill_plan(l2,r2,l3,r3)
            steps += [(public._mm,(l3,r3),{'out':p3})]
            steps += _combine_plan(p3,p2)+_combine_plan(p2,p1)
            self.cache[shape]=(l1,r1,p1,tuple(steps))
        out=fnp.empty((m,n),dtype=fnp.float32)
        left,right,products,steps=self.cache[shape]
        public._fill_batched_operands_d3(a,b,left,right)
        for op,args,kwargs in steps:op(*args,**kwargs)
        public._combine_seven_products_d3(products,out)
        return out
    def transform(self,M,A):
        # Transpose so every result ends in n, sharing the same workspaces.
        if A.shape[1]==0:return A
        parts=[]
        for at in range(0,A.shape[1],4096):parts.append(self.multiply(A[:,at:at+4096].T,M.T).T)
        return fnp.concatenate(parts,axis=1)
    def slice(self,A,B):
        n=A.shape[0];out=fnp.zeros((n,n),dtype=fnp.float32)
        for at in range(0,A.shape[1],4096):
            a=A[:,at:at+4096];b=B[:,at:at+4096]
            left=fnp.concatenate((b*b,2*a*b),axis=1)
            right=fnp.concatenate((a.T,b.T),axis=0)
            out=out+self.multiply(left,right)/3
        return out
