#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 13:53:18 2021

@author: yulong

https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_camp_boss/edit?language_uid=python3

下記の問題をプログラミングしてみよう！
A さんと B さんは次の操作を交互に繰り返すことで陣取りゲームをしようと考えました。 2 人の操作によって盤面が変化しなくなったらゲームを終了します。

・ 現在の陣地から上下左右に 1 マス移動することで到達できる、まだ誰の陣地でもない全てのマスを新たに陣地にする。ただし、障害物( # )のマスは陣地にできない。新たに陣地にできるマスが無い場合、何もしない。

盤面の情報と、先攻のプレイヤーの名前が与えられます。
盤面では、はじめに A さんのいるマスを 'A' , B さんのいるマスを 'B' で表します。
ゲーム終了時に A さん、 B さん、それぞれの陣地のマス数と勝った人の名前を出力してください。
なお、引き分けにはならないことが保証されています。

例として、ゲームが次のような状態でスタートした場合、

・ Aさんが先攻のときは次のような結果になるので、




6 3
A

と出力してください。

・ Bさんが先攻のときは次のような結果になるので、



3 6
B

と出力してください。
▼　下記解答欄にコードを記入してみよう

入力される値
H W     
N       
S_0     
...     
S_(H-1)


・ 1 行目では、マップの行数 H , 列数 W が与えられます。
・ 2 行目では、先攻のプレイヤーの名前 N が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。(0 ≦ j < W)

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
2 行の出力
二人のマス数の間には半角スペースを 1 つ出力してください。

A さんの陣地のマス数 B さんの陣地のマス数
勝者の名前

条件
すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ H, W ≦ 1000
・ N は 'A' か 'B'
・ S は W 文字の文字列
・ S の各文字は '.', '#', 'A', 'B'のいずれか
・ 'A' , 'B' のマスは１つ
・ 必ずゲームの勝者が決定する

入力例1
3 3
A
A..
...
..B

出力例1
6 3
A

入力例2
3 3
B
A.B
...
...

出力例2
3 6
B
"""
"""
# get h w first player and box
h,w=map(int,input().split())
p=str(input())
s=[list(input()) for _ in range(h)]

# find which one in box go first
sy1=[];sx1=[];sy2=[];sx2=[];
for sy in range(h):
    for sx in range(w):
        if s[sy][sx]==p:
            sy1.append(sy)
            sx1.append(sx)
        if s[sy][sx]!=p and s[sy][sx]!="." and s[sy][sx]!="#":
            sy2.append(sy)
            sx2.append(sx)    
flag=True
while step:
    (flag,s,y,x)=move(s,sy1,sx1)
    (flag,s,y,x)=move(s,sy2,sx2)   
if flag:
    x=[];y=[];
    x=sx1;y=sy1; 
    return(s,y,x)
    step=step+1
else:
    break

def move(s,y,x):
# move a step
# y and x are list of initial cells
# s is box
# output canbe final box and     
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
    return(flag,s,sy1,sx1)
    
    
        if flag:
            x=[];y=[];
            x=sx1;y=sy1; 
            return(s,y,x)
            step=step+1
        else:
            break
"""

H, W = map(int, input().split())
ab = input()
s = [list(input()) for _ in range(H)]
count = 0
aadd = 0
sums = [1, 1]
flag_pass = True
ab_point = [[], []]

if ab == "B":
    count += 1
    aadd += 1

for y in range(H):
    for x in range(W):
        if s[y][x] == "A":
            ab_point[0].append([y, x, aadd])
        if s[y][x] == "B":
            ab_point[1].append([y, x, 0])


while len(ab_point[0]) > 0 or len(ab_point[1]) > 0:
    if len(ab_point[count % 2]) == 0:
        count += 1
        flag_pass = False

    [y, x, n] = ab_point[count % 2][0]

    if count / 2 < n and flag_pass:
        count += 1
        [y, x, n] = ab_point[count % 2][0]

    ab_point[count % 2].pop(0)
    ab = "A" if count % 2 == 0 else "B"

    if y > 0 and s[y - 1][x] == ".":
        s[y - 1][x] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y - 1, x, n + 1])
    if y < H - 1 and s[y + 1][x] == ".":
        s[y + 1][x] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y + 1, x, n + 1])
    if x > 0 and s[y][x - 1] == ".":
        s[y][x - 1] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y, x - 1, n + 1])
    if x < W - 1 and s[y][x + 1] == ".":
        s[y][x + 1] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y, x + 1, n + 1])


print(sums[0], sums[1])
if sums[0] > sums[1]:
    result = "A"
elif sums[0] == sums[1]:
    result = "Draw"
else:
    result = "B"
print(result)