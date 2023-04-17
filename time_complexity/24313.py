# 백준 24313번 문제
# 문제링크>> https://www.acmicpc.net/problem/24313

a1, a2 = map(int, input().split())
c = int(input())
n = int(input())
f = a1 * n + a2
g = n

if(f <= c*g and c >= a1):
    print(1)
else:
    print(0)
