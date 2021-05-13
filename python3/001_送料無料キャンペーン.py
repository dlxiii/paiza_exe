#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:35:51 2021

@author: yulong
"""

a,b=map(int,input().split())
if a<3000:
    if b<=700:
        c=0.5*b
    else:
        c=b-350
else:
    if b<=700:
        c=0
    else:
        c=b-700
print("{:.0f}".format(a+c))

"""
import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
"""