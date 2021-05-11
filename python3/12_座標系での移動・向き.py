#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:37:50 2021

@author: yulong

開始時点の y , x 座標 と向いている方角 D が与えられます。
続く1行で移動の向き d が与えられるので、その向きに移動した後の y , x 座標 を答えてください。
移動前に向いている方角によって同じ移動の向きでも座標の変化が違うことに気をつけてください。
なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。
以下の図を参考にしてみてください。






入力される値
Y X D       
d


・ 1 行目には、開始時点の y , x 座標を表す Y , X,　現在の向いている方角を表す文字 D が与えられます。
・ 2 行目には、移動の向きを表す文字 d が与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
1 行での出力
・ 移動した後の y , x 座標を出力してください。


y x
条件
すべてのテストケースにおいて、以下の条件をみたします。
・ -100 ≦ X, Y ≦ 100
・ D は、N, S, E, W のいずれかでそれぞれ 北・南・東・西 を意味する。
・ d は、L, R のいずれかでそれぞれ 左・右 に １ マス進むことを表す。

入力例1
4 2 N
R

出力例1
4 3

入力例2
6 9 E
R

出力例2
7 9
"""

def move(dirc, zuoyou):
    if dirc == "N":
        if zuoyou == "R":
            return [0,1]
        else:
            return [0,-1]
    elif dirc == "S":
        if zuoyou == "L":
            return [0,1]
        else:
            return [0,-1]
    elif dirc == "E":
        if zuoyou == "R":
            return [1,0]
        else:
            return [-1,0]
    elif dirc == "W":
        if zuoyou == "R":
            return [1,0]
        else:
            return [-1,0]
    else:
        print("Wrong input")
    
Y,X,D = map(str,input().split())
d = str(input())
Y = int(Y)
X = int(X)
y,x = move(D,d)
print (Y+y,X+x)