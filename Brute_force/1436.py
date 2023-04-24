# 백준 1436번 문제
# 문제링크>> https://www.acmicpc.net/problem/1436

n = int(input())
cnt = 0
result = 666
 
while True:
    if '666' in str(result):
        cnt += 1
 
    if cnt == n:
        break
 
    result += 1
 
print(result)
