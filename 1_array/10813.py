# 백준 10813번 문제
# 문제링크>> https://www.acmicpc.net/problem/10813
n, m = map(int, input().split())
a = []

for c in range(1, n+1):
    a.append(c)
# basket : 0, 1, 2, 3, 4
# ball   : 1, 2, 3, 4, 5

for d in range(m):
    i, j = map(int, input().split())
    a[i-1], a[j-1] = a[j-1], a[i-1]

for s in a:   
   print(s, end=" ")
