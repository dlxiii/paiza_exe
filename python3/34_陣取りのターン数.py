#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 13:27:33 2021

@author: yulong

https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_camp_step5?language_uid=python3

下記の問題をプログラミングしてみよう！
盤面の情報と '?' でマスを塗る距離の個数 N, '?' でマスを塗るときの距離 l_i が与えられます。
現在プレイヤーのいるマスは '＊' になっており、そのマスはプレイヤーの陣地です。
プレイヤーは次の操作をできなくなるまで続けます。

・ プレイヤーは現在の陣地から１マス移動することで到達できるマスをプレイヤーの陣地にして、 '*' にする。
ただし、障害物( '#' )のマスは陣地にできない。また、プレイヤーの開始時の位置からの距離が l_i であるとき、 '*' の代わりに '?' にする。

なお、はじめにプレイヤーのいるマスの開始時の位置からの距離は 0 とします。

入力される値
H W N       
S_0     
...     
S_(H-1)     
l_1     
...     
l_N


・ 1 行目では、盤面の行数 H , 列数 W , l の入力の回数 N が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。(0 ≦ j < W)
・ 続く N 行では、 '?' でマスを塗るときの開始時の位置からの距離 l_i が与えられます。(1 ≦ i ≦ N)

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
H 行での出力

条件
すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ H , W , N ≦ 20
・ 0 ≦ l_i ≦ 50
・ S は W 文字の文字列
・ S の各文字は '.' または '*' または '#'
・ '*' のマスは１つ

入力例1
3 3 2
*..
...
...
1
3

出力例1
*?*
?*?
*?*

入力例2
10 10 5
##*#####..
..........
.#.#......
##..#.....
#########.
..........
..........
##########
..........
..........
1
4
5
7
9

出力例2
##*#####*?
**?**??*?*
?#*#??*?*?
##*?#*?*?*
#########*
**********
**********
##########
..........
..........
"""

# give h and w
h,w,n=map(int,input().split())
# give string box
s=[list(input()) for _ in range(h)]
o=[int(input()) for _ in range(n)]
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
            if  (step in o):
                s[y[idx]][x[idx]-1]="?"
            else:
                s[y[idx]][x[idx]-1]="*"
            sy1.append(y[idx])
            sx1.append(x[idx]-1)
            flag=True
        if x[idx]<w-1 and s[y[idx]][x[idx]+1]==".":
            if  (step in o):
                s[y[idx]][x[idx]+1]="?"
            else:
                s[y[idx]][x[idx]+1]="*"
            sy1.append(y[idx])
            sx1.append(x[idx]+1)
            flag=True
        if y[idx]>0 and s[y[idx]-1][x[idx]]==".":
            if  (step in o):
                s[y[idx]-1][x[idx]]="?"
            else:
                s[y[idx]-1][x[idx]]="*"
            sy1.append(y[idx]-1)
            sx1.append(x[idx])
            flag=True
        if y[idx]<h-1 and s[y[idx]+1][x[idx]]==".":
            if  (step in o):
                s[y[idx]+1][x[idx]]="?"
            else:
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