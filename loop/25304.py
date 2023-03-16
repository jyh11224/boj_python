# 백준 25304번 문제
# 문제링크>> https://www.acmicpc.net/problem/25304
x = int(input())
n = int(input())
m=0
sum=0

while(m<n):
    a, b = map(int, input().split())
    sum += (a * b)
    m += 1

if(x == sum):
    print("Yes")
else:
    print("No")
