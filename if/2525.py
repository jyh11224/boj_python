# 백준 2525번 문제
# 문제링크>> https://www.acmicpc.net/problem/2525
h,m= map(int,input().split())
oven = int(input())
h += oven//60 
m += oven%60
if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h,m)
