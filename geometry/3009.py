# 백준 3009번 문제
# 문제링크>> https://www.acmicpc.net/problem/3009
x_list = []
y_list = []

for _ in range(3):
    n,m = map(int, input().split())
    x_list.append(n)
    y_list.append(m)

for i in range(3):
    if(x_list.count(x_list[i]) == 1):
        print(x_list[i], end=' ')
        break
for i in range(3):
    if(y_list.count(y_list[i]) == 1):
        print(y_list[i])
        break
