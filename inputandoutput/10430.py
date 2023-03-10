# 백준 10430번 문제
# 문제링크>> https://www.acmicpc.net/problem/10430
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
