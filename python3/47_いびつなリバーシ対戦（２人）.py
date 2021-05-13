#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:59:22 2021

@author: yulong

下記の問題をプログラミングしてみよう！
A さんと B さんの 2 人でいびつなリバーシの対戦をします。
盤面・ターン数・各行動で石を置く座標についての情報が与えられます。
盤面に穴の空いているマスは # ,何も置かれていないマスは . になっています。
プレイヤーは次の操作を 1 回ずつ交互に合計 N 回繰り返します。なお、先攻は A さんです。

・ A さんは盤面のマス(Ya_i, Xa_i)に、Bさんは盤面のマス(Yb_i, Xb_i)に石を置きます。すでに相手の石が置かれている場合は相手の石を自分の石に置き換えます。
次に、縦横斜めに自分の石ではさんだ連続した穴の空いていないマスに自分の石をおきます。この時、既に相手の石が置かれている場合は相手の石を自分の石に置き換えます。
新たに置いた石によってさらに石が置けるようになった場合でもその時点で操作を終える。

操作を終えた後の盤面を出力してください。ただし、A さんの石が置かれているマスを 'A' , B さんの石が置かれているマスを 'B' として出力してください。
なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

例として、灰色のマスを穴の空いているマスとしたときに、
図 1 のような盤面のとき赤いマスに A さんが石を置くと図 2 のようになり、図 3 のような盤面のとき赤いマスに B さんが石を置くと図 4 のようになります。


図１

図２

図３

図４

入力される値
H W N       
S_0     
...     
S_(H-1)     
Ya_1 Xa_1       
Yb_1 Xb_1       
...     
Ya_N Xa_N       
Yb_N Xb_N


・ 1 行目では、盤面の行数 H ,列数 W , 各プレイヤーのターン数 N が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。
・ 続く 2 * N 行のうち 2 * i + 1 行目 (0 ≦ i ≦ N - 1) には、i 回目の操作で A さんが石を置く座標 Y_i X_i が与えられます。
2 * i 行目 (1 ≦ i ≦ N) には、i 回目の操作で B さんが石を置く座標 Y_i X_i が与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
H 行での出力

条件
すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ H, W, N ≦ 20
・ 0 ≦ Y_i < H, 0 ≦ X_i < W
・ S は W 文字の文字列
・ S の各文字は '.' または '#'
・ S[Ya_i][Xa_i] = '.'
・ S[Yb_i][Xb_i] = '.'

入力例1
3 3 2
...
...
.#.
0 0
2 0
0 2
2 2

出力例1
AAA
...
B#B

入力例2
5 5 3
....#
.....
.....
.....
.#...
0 0
4 0
2 2
4 2
3 4
1 1

出力例2
A...#
.B...
..A..
....A
B#B..
"""

H, W, N = map(int, input().split())
s = [list(input()) for _ in range(H)]
points = [list(map(int, input().split())) for _ in range(N * 2)]
player = "A"


def check_diagonal(x, y, s, player):
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
                ):
                    break
                if s[y + i * lr2][x + i * lr1] == player:
                    for j in range(1 + i):
                        s[y + j * lr2][x + j * lr1] = player
                    break
                if s[y + i * lr2][x + i * lr1] == "#":
                    break


def check_row(x, y, s, player):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if x + i * lr < 0 or x + i * lr >= W:
                break
            if s[y][x + i * lr] == player:
                for j in range(1 + i):
                    s[y][x + j * lr] = player
                break
            if s[y][x + i * lr] == "#":
                break


def check_column(x, y, s, player):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if y + i * lr < 0 or y + i * lr >= H:
                break
            if s[y + i * lr][x] == player:
                for j in range(1 + i):
                    s[y + j * lr][x] = player
                break
            if s[y + i * lr][x] == "#":
                break

for y, x in points:
    s[y][x] = player
    check_row(x, y, s, player)
    check_column(x, y, s, player)
    check_diagonal(x, y, s, player)
    if player == "A":
        player = "B"
    else:
        player = "A"

for y in range(H):
    for x in range(W):
        print(s[y][x], end="")
    print()