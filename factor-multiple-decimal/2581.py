# 백준 2581번 문제
# 문제링크>> https://www.acmicpc.net/problem/2581
m = int(input())
n = int(input())

b = []

for i in range(m, n+1):
    count = 0
    for j in range(1, i+1):    
        if(i % j == 0):
            count += 1
    if(count == 2):
        b.append(i)

if(len(b) == 0):
    print(-1)
else:
    print(sum(b))
    print(min(b))
