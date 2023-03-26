# 백준 3052번 문제
# 문제링크>> https://www.acmicpc.net/problem/3052
b = []
for i in range(10):
    a = int(input())
    b.append(a%42)
c = set(b)
print(len(c))
