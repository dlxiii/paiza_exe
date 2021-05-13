#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:58:42 2021

@author: yulong

下記の問題をプログラミングしてみよう！
盤面についての情報が与えられます。
はじめ、プレイヤーの石が置かれているマスは ＊ になっており、盤面に穴の空いているマスは # ,何も置かれていないマスは . になっています。

プレイヤーは盤面の ! のマスに石を置き、
縦横斜めに自分の石ではさんだ連続した穴の空いていないマスの間に自分の石を置きます。
新たに置いた石によってさらに石が置けるようになった場合でもその時点で操作を終える。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

例として、灰色のマスを穴の空いているマスとしたときに、
図 1 のような盤面のとき赤いマスに石を置くと図 2 のようになり、図 3 のような盤面のとき赤いマスに石を置くと図 4 のようになります。


図１

図２

図３

図４

この操作を終えた後の盤面を出力してください。

入力される値
H W     
S_0     
...     
S_(H-1)


・ 1 行目では、盤面の行数 H ,列数 W が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
H 行での出力

条件
すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ H, W ≦ 20
・ S は W 文字の文字列
・ S の各文字は '.' または '*' または '#' または '!'
・ ! のマスは １ つ

入力例1
3 3
!.*
...
*.*

出力例1
***
**.
*.*

入力例2
5 5
*.*.*
.....
*#!.*
...#*
*.***

出力例2
*.*.*
.***.
*#***
.**#*
*.***
"""

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]


def check_diagonal(x, y, s):
    for lr1 in range(-1, 2, 2):
        for lr2 in range(-1, 2, 2):
            i = 0
            while True:
                i += 1
                if (
                    x + i * lr1 < 0
                    or x + i * lr1 >= W
                    or y + i * lr2 < 0
                    or y + i * lr2 >= H
                    or s[y + i * lr2][x + i * lr1] == "#"
                ):
                    break
                if s[y + i * lr2][x + i * lr1] == "*":
                    for j in range(1 + i):
                        s[y + j * lr2][x + j * lr1] = "*"
                    break


def check_row(x, y, s):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if x + i * lr < 0 or x + i * lr >= W or s[y][x + i * lr] == "#":
                break
            if s[y][x + i * lr] == "*":
                for j in range(1 + i):
                    s[y][x + j * lr] = "*"
                break


def check_column(x, y, s):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if y + i * lr < 0 or y + i * lr >= H or s[y + i * lr][x] == "#":
                break
            if s[y + i * lr][x] == "*":
                for j in range(1 + i):
                    s[y + j * lr][x] = "*"
                break


X, Y = None, None
for y in range(H):
    for x in range(W):
        if s[y][x] == "!":
            X = x
            Y = y
            break

s[Y][X] = "*"
check_row(X, Y, s)
check_column(X, Y, s)
check_diagonal(X, Y, s)

for y in range(H):
    for x in range(W):
        print(s[y][x], end="")
    print()