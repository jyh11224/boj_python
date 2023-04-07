# 백준 11005번 문제
# 문제링크>> https://www.acmicpc.net/problem/11005
import sys

input = sys.stdin.readline

tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = []

n, b = map(int, input().split())

while n != 0:
    answer.append(tmp[n%b])
    n = n // b

print(*answer[::-1], sep = '')
