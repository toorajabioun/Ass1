# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:45:55 2017

@author: tooraj
"""

def multgood(x,y):
    
    #x=str(X)
    #y=str(Y)
    
    n=len(x)
    m=len(y)
    
    if m>n:
        n=m
    
    if int(n/2)!=n/2:
        n=n+1
    n2=int(n/2)
    a=x[:-n2]
    if len(a)==0:
        a='0'
    b=x[-n2:]
    c=y[:-n2]
    if len(c)==0:
        c='0'
    d=y[-n2:]
    
    if n>2:
        ac=multgood(a,c)
        bd=multgood(b,d)
        step3=str(int(multgood(str(int(a)+int(b)),str(int(c)+int(d))))-int(ac)-int(bd))
    else:
        ac=str(int(a)*int(c))
        bd=str(int(b)*int(d))
        step3=str((int(a)+int(b))*(int(c)+int(d))-int(ac)-int(bd))
    
    
    nbd=len(bd)
    nac=len(ac)
    
    
    if nbd<n2:
        bd='0'*(n2-nbd)+bd
    elif nbd>n2:
        co=int(bd[:int(nbd-n2)])
        bd=bd[int(nbd-n2):]
        step3=str(int(step3)+co)

    nstep3=len(step3)
    if nstep3<n2:
        step3='0'*(n2-nstep3)+step3
    elif nstep3>n2:
        co=int(step3[:int(nstep3-n2)])
        step3=step3[int(nstep3-n2):]
        ac=str(int(ac)+co)
    res=ac+step3+bd
    return res
