#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:51:22 2021

@author: yulong

下記の問題をプログラミングしてみよう！
盤面の情報が与えられます。
現在プレイヤーのいるマスは '＊' になっており、そのマスはプレイヤーの陣地です。
プレイヤーは次の操作をできなくなるまで続けます。

・ プレイヤーは現在の陣地から上下左右に １ マス移動することで到達できるマスをプレイヤーの陣地にする。ただし障害物( '#' )のマスは陣地にできない。

操作を終えた後のプレイヤーの陣地を '＊' にした盤面を出力してください。







入力される値
H W     
S_0     
...     
S_(H-1)


・ 1行目では、盤面の行数 H , 列数 W が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。(0 ≦ j < W)

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
操作後の盤面を H 行で出力してください。

条件
すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ H, W ≦ 20
・ S は W 文字の文字列
・ S の各文字は '.' または '*' または '#'
・ '*' のマスは １ つ

入力例1
3 3
*..
...
...

出力例1
***
***
***

入力例2
3 3
*.#
..#
##.

出力例2
**#
**#
##.
"""



# give h and w
h,w=map(int,input().split())
# give string box
s=[list(input()) for _ in range(h)]
# 1 step of moving
x=[];y=[];
step=1
for sy in range(h):
    for sx in range(w):
        if s[sy][sx]=="*":
            y.append(sy)
            x.append(sx)
while step:
    flag=False
    sx1=[];sy1=[]; 
    for idx in range(len(y)):
        if x[idx]>0 and s[y[idx]][x[idx]-1]==".":
            s[y[idx]][x[idx]-1]="*"
            sy1.append(y[idx])
            sx1.append(x[idx]-1)
            flag=True
        if x[idx]<w-1 and s[y[idx]][x[idx]+1]==".":
            s[y[idx]][x[idx]+1]="*"
            sy1.append(y[idx])
            sx1.append(x[idx]+1)
            flag=True
        if y[idx]>0 and s[y[idx]-1][x[idx]]==".":
            s[y[idx]-1][x[idx]]="*"
            sy1.append(y[idx]-1)
            sx1.append(x[idx])
            flag=True
        if y[idx]<h-1 and s[y[idx]+1][x[idx]]==".":
            s[y[idx]+1][x[idx]]="*"
            sy1.append(y[idx]+1)
            sx1.append(x[idx])
            flag=True
    # finishing 1 step of moving and judge if continue
    if flag:
        x=[];y=[];
        x=sx1;y=sy1; 
        step=step+1
    else:
        break
# outputs
for y in range(h):
    print("".join(s[y]))
