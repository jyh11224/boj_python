# 백준 1978번 문제
# 문제링크>> https://www.acmicpc.net/problem/1978
n = int(input())
count = 0
a = list(map(int, input().split()))

for i in range(n):
    b = []
    for j in range(1,1001):
        if((a[i] % j) == 0):
            b.append(j)
    if(len(b) == 2):
        count += 1
print(count)
