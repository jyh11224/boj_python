# 백준 2439번 문제
# 문제링크>> https://www.acmicpc.net/problem/2439
t = int(input())
a=1
for i in range(1, t+1):
    print(("*" * a).rjust(t))   
    a += 1
