# 백준 10810번 문제
# 문제링크>> https://www.acmicpc.net/problem/10810
n, m = map(int, input().split())

a = [0]*n

for b in range(m):
    i,j,k = map(int, input().split())
    for c in range(i-1,j):
        a[c] = k
for d in a:
    print(d, end=" ")
