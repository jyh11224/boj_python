# 백준 2720번 문제
# 문제링크>> https://www.acmicpc.net/problem/2720

import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    q = 0
    d = 0   
    n = 0
    p = 0
    i = int(input())
    while(i != 0):
        if i >= 25:
            i -= 25
            q += 1       
        elif i >= 10:
            i -= 10
            d += 1
        elif i >= 5:
            i -= 5
            n += 1
        elif i >= 1:
            i -= 1
            p += 1
    print(q, d, n, p)
