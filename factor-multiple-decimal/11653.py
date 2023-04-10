# 백준 11653번 문제
# 문제링크>> https://www.acmicpc.net/problem/11653
import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(' ')

for i in range(2,n+1):
    if n % i == 0:
        while n % i == 0:
            print(i)
            n =  n/i
