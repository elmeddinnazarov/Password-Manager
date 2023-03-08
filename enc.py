import random
import string
import textwrap
i=len
k=str
u=int
F=range
def M(s):
    h=textwrap.wrap(s,1)
    e=i(h)
    w=i(k(e))
    T=u(119/e)
    j=T
    s=i(k(j))
    l=string.ascii_letters+string.digits+string.digits+string.punctuation
    y=''.join(random.choice(l)for i in F(120))
    for g in h:
        y=y[:T]+g+y[T+1:]
        T+=j
    y=k(e).rjust(2,"&")+k(y)[10]+k(w)+k(y)+k(j).rjust(2,"%")+k(y)[10]+k(s)
    return y

def Y(c):
    S=[]
    G=c[:4]
    if not "&" in G:
        N=G[:2]
    else:
        N=G[1]
    N=u(N)
    o=c[-4:]
    if not "%" in o:
        V=o[:2]
    else:
        V=o[1]
    V=u(V)
    z=c[4:-4]
    d=V
    for pw in F(N):
        S.append(z[V])
        V+=d
    H="".join(S)
    return H

