# 백준 2903번 문제
# 문제링크>> https://www.acmicpc.net/problem/2903
n = int(input())
a = [4]
f = 2
b = 1
sum = 0
for i in range(1, n+1):
    f += b
    sum = f ** 2
    a.append(sum)
    b = b * 2
print(a[n])
