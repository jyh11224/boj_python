# 백준 11021번 문제
# 문제링크>> https://www.acmicpc.net/problem/11021
t = int(input())
x = 1
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f"Case #{x}:",a+b)
    x += 1
