# 백준 2869번 문제
# 문제링크>> https://www.acmicpc.net/problem/2869
a,b,v = map(int, input().split())

if (v-b)%(a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)
