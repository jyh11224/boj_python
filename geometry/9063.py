# 백준 9063번 문제
# 문제링크>> https://www.acmicpc.net/problem/9063

n = int(input())

x = []
y = []

for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

print((max(x) - min(x)) * ((max(y) - min(y))))
