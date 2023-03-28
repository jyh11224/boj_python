# 백준 11720번 문제
# 문제링크>> https://www.acmicpc.net/problem/11720
a = int(input())
b = str(input())
sum = 0
for i in range(a):
    sum += int(b[i])
print(sum)
