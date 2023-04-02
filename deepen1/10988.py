# 백준 10988번 문제
# 문제링크>> https://www.acmicpc.net/problem/10988
s = str(input())

if(s == s[::-1]):
    print(1)
else:
    print(0)
