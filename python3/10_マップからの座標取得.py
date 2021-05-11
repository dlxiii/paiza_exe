#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:53:41 2021

@author: yulong

下記の問題をプログラミングしてみよう！
マップの行数 H と列数 W とマップを表す H 行 W 列の文字列 S_1 ...S_H が与えられます。
要素が '#' になっているマスの y , x 座標 を答えてください。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

入力される値
H W     
S_0     
...     
S_(H-1)


・ 1 行目には盤面の行数を表す整数 H , 盤面の列数を表す整数 W が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。(0 ≦ j < W)

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
1行の出力
- 要素が '#' になっているマスの y , x 座標を 1 行で出力してください。

y x
条件
すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ H, W ≦ 20
・ S は W 文字の文字列
・ S の各文字は '.' または '#'
・ '#' のマスは必ず１つ

入力例1
1 1
#

出力例1
0 0

入力例2
3 3
.#.
...
...

出力例2
0 1
"""

H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
for y in range(H):
    for x in range(W):
        if S[y][x] == "#": print()
        