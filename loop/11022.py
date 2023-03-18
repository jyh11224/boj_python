# 백준 11022번 문제
# 문제링크>> https://www.acmicpc.net/problem/11022
t = int(input())
x = 1
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f"Case #{x}: {a} + {b} =",a+b)
    x += 1
