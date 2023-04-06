# 백준 10798번 문제
# 문제링크>> https://www.acmicpc.net/problem/10798
a = []
b = []
c = []
for i in range(5):
    s = str(input())
    b.append(len(s))
    a.append(s)

for j in range(max(b)):
    for k in range(5):
        if (j < b[k]):
            c += a[k][j]
for d in c:
    print(d, end = '')
