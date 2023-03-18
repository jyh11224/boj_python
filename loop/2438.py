# 백준 2438번 문제
# 문제링크>> https://www.acmicpc.net/problem/2438
t = int(input())
a=2
for i in range(1, t+1):
    for k in range(1, a):
        print("*", end="")
    a += 1
    print()
