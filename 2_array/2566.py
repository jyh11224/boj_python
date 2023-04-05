# 백준 2566번 문제
# 문제링크>> https://www.acmicpc.net/problem/2566
a = []
b = []
c = []
for i in range(9):
    a.append(list(map(int, input().split())))

for num in a:
    b.append(max(num))

c = a[b.index(max(b))]

print(max(b))
print(b.index(max(b))+1, end = ' ')
print(c.index(max(b))+1)
