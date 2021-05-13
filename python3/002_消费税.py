#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:54:25 2021

@author: yulong
"""

a,b=map(int,input().split())
c = b+b*a*0.01
c_int_roundup = int(c+0.5)
print("%d" % c_int_roundup)