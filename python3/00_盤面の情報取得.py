#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:24:39 2021

@author: yulong

行数 H , 列数 W の盤面があり、各マスには文字が 1 つだけ書かれています。
盤面と N 個の y , x 座標 が与えられるので、与えられた座標の文字を順に出力してください。
なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

入力される値
H W N   
S_0     
...     
S_(H-1)    
y_1 x_1     
...     
y_N x_N

・ 1 行目には盤面の行数を表す整数 H , 盤面の列数を表す整数 W , 与えられる座標の数を表す整数 N が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。
・ 続く N 行 には、文字を答えるための y_i , x_i 座標が与えられます。(1 ≦ i ≦ N)

期待する出力
N 行の出力


A_1        
...     
A_N


・ i 行目 (1 ≦ i ≦ N) には、 i 番目の座標 y_i, x_i の盤面の文字 A_i を出力してください。

すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ H , W ≦ 20
・ 1 ≦ N ≦ H × W
・ 0 ≦ y_i < H , 0 ≦ x_i < W (0 ≦ i < N)
・ S は W 文字の文字列
・ S の各文字は . または #

入力例1
3 3 2
###
###
...
2 2
1 1

出力例1
.
#

入力例2
2 2 1
#.
.#
0 1

出力例2
.
"""

H, W, N = map(int, input().split())
S = [list(input()) for _ in range(H)]
for _ in range(N):
  y, x = map(int, input().split())
  print(S[y][x])
 
"""
H,W,N = map(int, input().split())
S = [list(input())]
for _ in range(H-1):
    S.append(list(input()))
for _ in range(N):
    y,x = map(int, input().split())
    print(S[y][x])
    
盤面の情報取得 Key point
map函数
input函数
split函数
循环构造数组
_ in range()
list函数
"""
    
    

