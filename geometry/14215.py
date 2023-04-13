# 백준 14215번 문제
# 문제링크>> https://www.acmicpc.net/problem/14215
li = sorted(map(int, input().split()))
res = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
print(res)
