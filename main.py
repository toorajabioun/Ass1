# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:00:16 2017

@author: tooraj
"""

from multgood import multgood
import time
#inputs:
x='3141592653589793238462643383279502884197169399375105820974944592'
y='2718281828459045235360287471352662497757247093699959574966967627'
x=x*1
y=y*1
n=len(x)
t1=time.clock()
z=multgood(x,y)
print(z)
print('t1= '+str(time.clock()-t1))
X=int(x)
Y=int(y)
t1=time.clock()
z=X*Y
print(int(x)*int(y))
print('t2= '+str(time.clock()-t1))
