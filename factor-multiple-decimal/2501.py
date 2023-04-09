# 백준 2501번 문제
# 문제링크>> https://www.acmicpc.net/problem/2501
a = []

i, j = map(int, input().split())

for num in range(1, i+1):
    factor = i % num
    if(i % num == 0):
        a.append(num)
if(len(a) < j):
    print(0)
else:
    print(a[j-1])
