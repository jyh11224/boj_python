# 백준 2908번 문제
# 문제링크>> https://www.acmicpc.net/problem/2908
a, b = map(str, input().split())
new_a = int(str(a)[::-1])
new_b = int(str(b)[::-1])
if(new_a>new_b):
    print(new_a)
else:
    print(new_b)
