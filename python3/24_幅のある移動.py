#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 21:50:01 2021

@author: yulong

下記の問題をプログラミングしてみよう！
マップの行数 H と列数 W ,障害物を # で移動可能な場所を . で表した H 行 W 列のマップ S_1 ... S_H ,現在の座標 sy , sx ,移動の回数 N が与えられます。
はじめは北を向いています。
続けて N 回の移動の向き d_1 ... d_N と移動するマス数 l_1...l_N が与えられます。
各移動が可能である場合、スタート位置を含む移動の際に通ったマップのマスを * に変更してください。移動できない場合、壁やマップの端までできる限り移動をして通ったマップのマスを * に変更したのち、以降の移動を打ち切ってください。
移動が終了した時のマップを出力してください。
移動可能であるということは、以下の図の通り
「今いるマスから移動先のマスまでの間の全てのマスが移動可能である かつ 移動先がマップの範囲外でない」 ということを意味します。
なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。




入力される値
H W sy sx N        
S_0     
...     
S_(H-1)     
d_1 l_1     
...     
d_N l_N


・ 1 行目には盤面の行数を表す整数 H , 盤面の列数を表す整数 W , 現在の y, x 座標を表す sy sx , 移動する回数 N が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。(0 ≦ j < W)
・ 続く N 行のうち i 行目 (1 ≦ i ≦ N) には、i 回目の移動の向き d_i と移動のマス数 l_i が与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
H 行の出力(マップの出力)

条件
すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ H, W ≦ 20
・ 1 ≦ N ≦ 100
・ 0 ≦ sy < H , 0 ≦ sx < W
・ 1 ≦ l_i ≦ 20
・ S_i は W 文字の文字列
・ マップ上の (sy, sx) のマスは必ず '.'
・ S の各文字は '.' または '#'
・ d_i は、 L, R のいずれかであり、それぞれ 左・右 を意味します。

入力例1
10 10 4 5 3
.......#..
..........
..........
#.........
..........
......#...
..........
....#.....
...#......
..........
L 3
R 1
R 3

出力例1
.......#..
..........
..........
#.****....
..****....
......#...
..........
....#.....
...#......
..........

入力例2
15 15 10 7 5
...............
...............
##.............
........#......
....#..........
...........#.#.
........#......
#...#...#......
#......#.......
...............
.#.............
..#............
...............
.......#..#...#
..........#....
L 3
L 1
R 2
R 1
L 1

出力例2
...............
...............
##.............
........#......
....#..........
...........#.#.
........#......
#...#...#......
#......#.......
...............
.#..****.......
..#**..........
...............
.......#..#...#
..........#....
"""

"""
def move(m,f,x,y,st):
    if f=="N":
        if m=="L":
            x-=st; f="W"
        else:
            x+=st; f="E"
    elif f=="E":
        if m=="L":
            y-=st; f="N"
        else:
            y+=st; f="S"
    elif f=="S":
        if m=="L":
            x+=st; f="E"
        else:
            x-=st; f="W"
    elif f=="W":
        if m=="L":
            y+=st; f="S"
        else:
            y-=st; f="N"
    return(f,x,y)
    
def strait(x,y):
    if f=="N":
            y-=1;
    elif f=="E":
            x+=1;
    elif f=="S":
            y+=1;
    elif f=="W":
            x-=1;
    return(x,y)
    
def p(x,y,w,h):
    if x<0 or y<0 or x>w-1 or y>h-1:
        val=False
    else:
        if s[y][x]=="#":
            val=False
        else:
            val=True
    return(val)

h,w,sy,sx,n=map(int,input().split())
s=[list(input()) for _ in range(h)]
f="N"
s[sy][sx]="*"
for _ in range(n):
    m,st=map(str,input().split())
    st=int(st)
    (f,sx,sy)=move(m,f,sx,sy,1)
    if p(sx,sy,w,h):
        print(sy,sx)
        s[sy][sx]="*"
    else:
        print(sy,sx)
        print("Stop")
        break
    for _ in range(st-1):
        (sx,sy)=strait(sx,sy)
        if p(sx,sy,w,h):
            print(sy,sx)
            s[sy][sx]="*"
        else:
            print(sy,sx)
            print("Stop")
            break
    else:
        continue
    break
    
for y in range(h):
    print("".join(s[y]))
 """   
    
h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0
s[sy][sx] = "*"

for _ in range(int(n)):
    d_i, l_i = input().split()
    l_i = int(l_i)
    if d_i == "L":
        now = (3 + now) % 4
    else:
        now = (1 + now) % 4

    flag = False
    for i in range(l_i):
        if directions[now] == "N":
            sy -= 1
        elif directions[now] == "E":
            sx += 1
        elif directions[now] == "S":
            sy += 1
        elif directions[now] == "W":
            sx -= 1

        if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
            flag = True
            break
        else:
            s[sy][sx] = "*"

    if flag:
        break

for y in range(int(h)):
    print("".join(s[y]))

