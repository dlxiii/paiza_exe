#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:18:51 2021

@author: yulong

4 5 1
1 2 3 4
1 2
1 3
1 4
2 4
3 4
"""
def find_nodes(i,way):
    node=[]
    for idx_uv in range(len(way)):
        if i in way[idx_uv] and way[idx_uv][0]==i:
            node.append(way[idx_uv][1])
        elif i in way[idx_uv] and way[idx_uv][1]==i:
            node.append(way[idx_uv][0])
    return node

def find_color(a):
    a.sort()
    maxlabel = max(a,key=a.count)
    return maxlabel


n,m,k=map(int,input().split())
c0=list(map(int,input().split()))
way = [list(map(int, input().split())) for _ in range(m)]

c=c0
c_now=[]
color_list=[]

for _ in range(k):
    for idx_n in range(1,n+1):
        nodelist=find_nodes(idx_n,way)
        color_list=[c[i-1] for i in nodelist]
        c_now.append(find_color(color_list))
    c_nodelist=[]
    c=c_now
    c_now=[]

for idx_c in range(n):
    print(c[idx_c])

