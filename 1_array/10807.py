# 백준 10807번 문제
# 문제링크>> https://www.acmicpc.net/problem/10807
n = int(input())
a = list(map(int, input().split()))
v = int(input())
count = 0
for i in a:
    if(i == v):
        count += 1
print(count)
