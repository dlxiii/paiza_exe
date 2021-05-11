#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:05:27 2021

@author: yulong

下記の問題をプログラミングしてみよう！
開始時点の x , y 座標と移動の歩数 N が与えられます。
以下の図のように時計回りに渦を巻くように移動を N 歩行った後の x , y 座標 を答えてください。
なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。



入力される値
X Y N


・ 1 行で、開始時点の x , y 座標を表す X , Y, 移動の歩数 N が与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
1行での出力
・ 移動を N 歩行った後の x , y 座標を出力してください。


x y
条件
すべてのテストケースにおいて、以下の条件を満たします。
・ -100 ≦ X, Y ≦ 100
・ 0 ≦ N ≦ 100

入力例1
0 0 3

出力例1
0 1

入力例2
38 47 27

出力例2
41 47

第一时间内没有做出来，当时还想着写出公式来。
实际上这是缘木求鱼的方法，编程的方法就是用笨方法解决问题。
想象一下这个逻辑。
每两行列是相同的格子后，就会增长格子。
比如11，22，33，44，55
如果在第一个相同行列中，如果达到最大计数，则进入第二个相同行列。
进入后，标注为第二个相同行列，计数清零。方向改变。
如果在第二个相同行列中，达到最大计数，则进入下一个行列。
进入后，重新标注为第一个相同行列，计数清零，方向改变，增大计数器。

"""

def move(direction,x,y):
    if direction == "N":
        y = y - 1
    elif direction == "E":
        x = x + 1
    elif direction == "S":
        y = y + 1
    elif direction == "W":
        x = x - 1
    return (x, y)

x,y,n = map(int,input().split())
directions = ["E","S","W","N"]
now_direction = 0
first = True
count = 0
max_count = 1
number = n

for _ in range(n):
    (x,y) = move(directions[now_direction],x,y)
    count = count + 1
    if first:
        if count == max_count:
            count = 0
            now_direction = (now_direction + 1)%4
            first = False
    elif count == max_count:
        count = 0
        max_count = max_count + 1
        now_direction = (now_direction + 1)%4
        first = True
print(x,y)


"""
def move(direction, x, y):
    if direction == "N":
        y = y - 1
    elif direction == "E":
        x = x + 1
    elif direction == "S":
        y = y + 1
    elif direction == "W":
        x = x - 1
    return (x, y)

x, y, n = map(int, input().split())
directions = ["E","S","W","N"]
now_direction = 0
count = 0
max_count = 1
first = True
step = 0

for _ in range(n):
    (x,y) = move(directions[now_direction],x,y)
    count = count + 1
    # 如果是转向后的第一行或第一列，而且是计数已满，则清空计数器，转换方向
    if first and count == max_count:
        first = False
        count = 0
        now_direction = (1 + now_direction) % 4
    # 如果计数已满，则清空计数器，增大计数器容量，并且转换方向
    elif count == max_count:
        first = True
        count = 0
        max_count += 1
        now_direction = (1 + now_direction) % 4    
    step = step + 1
    print("当前数字：",step)
    print("当前坐标：(",x,",",y,")")
    print("当前方向：",directions[now_direction])
    print("当前状态：",count,"/",max_count)
"""
"""
x, y, n = map(int, input().split())
directions = ["E", "S", "W", "N"]
now_direction = 0
count = 0
max_count = 1
first = True


def move(direction, x, y):
    if direction == "N":
        y -= 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y += 1
    elif direction == "W":
        x -= 1
    return (x, y)


for _ in range(n):
    (x, y) = move(directions[now_direction], x, y)
    count += 1
    if first and count == max_count:
        first = False
        count = 0
        now_direction = (1 + now_direction) % 4
    elif count == max_count:
        first = True
        count = 0
        max_count += 1
        now_direction = (1 + now_direction) % 4


print(x, y)
"""