# 백준 8393번 문제
# 문제링크>> https://www.acmicpc.net/problem/8393
n = int(input())
t=1
sum = 0
while(t <= n):    
    sum += t
    t += 1
print(sum)
