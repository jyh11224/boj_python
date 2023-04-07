# 백준 2292번 문제
# 문제링크>> https://www.acmicpc.net/problem/2292
n = int(input())
cnt = 1
num = 1
while(n > num):
    num += cnt*6
    cnt += 1
print(cnt)
