#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:19:59 2021

@author: yulong
"""

n=int(input())
a=list(map(int,input().split()))

out=[]

for i in range(n):
    b=[k for k in a]
    b.pop(i)
    maxvalue = max(b)
    out.append(maxvalue)

for i in range(len(out)):
    print(out[i])