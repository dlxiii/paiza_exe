#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 01:04:47 2021

@author: yulong

下記の問題をプログラミングしてみよう！
数列 A についての情報と、整数 K が与えられます。
次の条件を満たす A の部分列の最短の長さを答えてください。

・ 数列に含まれる全ての要素の積が K 以上である。

なお、数列の部分列とは、数列の連続した 1 つ以上の要素を取り出して作ることができる数列のことです。

▼　下記解答欄にコードを記入してみよう

入力される値
N　K            
A_1 A_2 ... A_N


・ 1 行目には、数列 A の要素数 N と、条件に使う整数 K が与えられます。
・ 2 行目には、数列 A の各要素 A_1, A_2 ... A_N が与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
期待する出力
条件を満たす A の部分列の最短の長さ

条件
すべてのテストケースにおいて、以下の条件をみたします。

・ 1 ≦ N ≦ 10 ^ 5
・ 1 ≦ K ≦ 10 ^ 10
・ A_i は、0, 1, 2のいずれか

入力例1
5 1
1 1 1 1 1

出力例1
1

入力例2
6 16
2 0 2 2 2 2

出力例2
4
"""

n, k = map(int, input().split())
numbers = list(map(int, input().split()))


def mul_list(data):
    result = 1
    for i in data:
        result *= i
    return result


count = float("inf")
start = 0
end = 0
while True:
    if end >= n or start > end:
        break
    if mul_list(numbers[start: end + 1]) >= k:
        if end - start + 1 < count:
            count = end - start + 1
        start += 1
    elif numbers[end] == 0:
        start = end + 1
        end += 1
    else:
        end += 1


print(count)