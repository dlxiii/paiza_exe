#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:51:20 2021

@author: yulong
"""

def move(y,x,d):
    if d=="N":
        y-=1
    elif d=="S":
        y+=1
    elif d=="W":
        x-=1
    elif d=="E":
        x+=1
    return(y,x)

n,m = map(int, input().split())
s = [list(input()) for _ in range(n)]

y=0;x=0;
count=0
while True:
    d=s[y][x] #next direction
    s[y][x]="#"
    y,x=move(y,x,d) #new location
    if y<0 or x<0 or y>n-1 or x>m-1:
        count+=1
        break
    if s[y][x]=="#":
        count+=1
        break
    count+=1

print (count)