#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:08:40 2021

@author: yulong

下記の問題をプログラミングしてみよう！
マップの行数 H と列数 W ,障害物を # ,移動可能な場所を . で表した H 行 W 列のマップ S_1 ... S_H が与えられます。
続けて現在の座標 sy , sx ,現在向いている方角 d ,１マス移動する方向 m が与えられるので、移動が可能かどうかを判定してください。
移動可能であるということは、以下の図の通り 「移動先が障害物でない かつ 移動先がマップの範囲外でない」 ということを意味します。
なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。




入力される値
H W　sy sx d m      
S_0     
...     
S_(H-1)


・ 1 行目には盤面の行数を表す整数 H , 盤面の列数を表す整数 W , 現在の y, x 座標を表す sy sx , 現在向いている方角 d , 1 マス移動する方向 m が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。(0 ≦ j < W)

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
移動が可能である場合 "Yes" を、不可能である場合 "No" を出力してください。

条件
すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ H, W ≦ 20
・ 0 ≦ sy < H , 0 ≦ sx < W
・ S_i は W 文字の文字列
・ マップ上の(sy, sx)のマスは必ず '.'
・ S の各文字は '.' または '#'
・ d は、 N, S, E, W のいずれかであり、それぞれ 北・南・東・西 を意味します。
・ m は、 L, R のいずれかであり、それぞれ 左・右 を意味します。

入力例1
2 6 0 4 E L
####..
##..#.

出力例1
No

入力例2
7 9 6 0 S R
..#.#..##
..#..#...
#.......#
#.#...###
#.##....#
.....#...
..##..#.#

出力例2
No
"""
def move(dirc,face,x,y):
    #(face,x,y)=move("L",0,x,y)
    if face=="N":
        if dirc=="L":
            x-=1; face="W"
        else:
            x+=1; face="E"
    elif face=="E":
        if dirc=="L":
            y-=1; face="N"
        else:
            y+=1; face="S"
    elif face=="S":
        if dirc=="L":
            x+=1; face="E"
        else:
            x-=1; face="S"
    elif face=="W":
        if dirc=="L":
            y+=1; face="S"
        else:
            y-=1; face="N"
    return(face,x,y)
    
h,w,sy,sx,d,m=map(str,input().split())
h=int(h);w=int(w);sy=int(sy);sx=int(sx);
s=[list(input()) for _ in range(h)]
face=d
dirc=m
(_,x,y)=move(dirc,face,sx,sy)
if x<0 or y<0 or x>w-1 or y>h-1:
    print("No")
else:
    if s[y][x]=="#":
        print("No")
    else:
        print("Yes")