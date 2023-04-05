# 백준 2738번 문제
# 문제링크>> https://www.acmicpc.net/problem/2738
n,m = map(int, input().split())
mat1 = []
mat2 = []
for i in range(n):
    a = list(map(int,input().split()))
    mat1.append(a)
for i in range(n):
    b = list(map(int,input().split()))
    mat2.append(b)
for j in range(n):
    for k in range(m):
       print(mat1[j][k] + mat2[j][k], end = ' ')
    print()
