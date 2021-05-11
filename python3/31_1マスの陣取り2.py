#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:24:26 2021

@author: yulong

下記の問題をプログラミングしてみよう！
盤面の情報が与えられます。現在プレイヤーのいるマスは '＊' になっており、そのマスはプレイヤーの陣地です。
プレイヤーは現在の陣地から上下左右に１マス移動することで到達できるマスをプレイヤーの陣地にします。
ただし、障害物( '#' ) のあるマスは陣地にできません。
プレイヤーの陣地を '＊' にした盤面を出力してください。

入力される値
H W     
S_0   
...     
S_(H-1)


・ 1 行目では、盤面の行数 H , 列数 W が与えられます。
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
...
.*.
...

出力例1
.*.
***
.*.

入力例2
6 6
......
...#..
..#*#.
......
......
......

出力例2
......
...#..
..#*#.
...*..
......
......
"""

# height and width
w,h=map(int,input().split())
# string box
s=[list(input()) for _ in range(h)]
# calculation: find * and give *
flag=False
for y in range(h):
    for x in range(w):
        if s[y][x]=="*":
            flag=True
            if x>0 and s[y][x-1]!="#":
                s[y][x-1]="*"
            if x<w-1 and s[y][x+1]!="#":
                s[y][x+1]="*"
            if y>0 and s[y-1][x]!="#":
                s[y-1][x]="*"
            if y<h-1 and s[y+1][x]!="#":
                s[y+1][x]="*"
            break # quit x loop after giving *
    if flag:
        break # quit y loop after giving *
# outputs
for y in range(h):
    print("".join(s[y]))