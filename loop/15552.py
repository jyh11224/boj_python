# 백준 15552번 문제
# 문제링크>> https://www.acmicpc.net/problem/15552
import sys

n = int(sys.stdin.readline())
a=0
while(a<n):
    c, d = map(int, sys.stdin.readline().split())
    print(c + d)
    a +=1
