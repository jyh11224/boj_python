# 백준 2675번 문제
# 문제링크>> https://www.acmicpc.net/problem/2675
t = int(input())

for i in range(t):
    r,s = input().split()
    r = int(r)
    s = str(s)
    for j in s:
        for k in range(r):
            print(j, end = "")
    print()
