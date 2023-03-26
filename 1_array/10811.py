# 백준 10811번 문제
# 문제링크>> https://www.acmicpc.net/problem/10811
n, m = map(int, input().split())
a = [i for i in range(1,n+1)]

for b in range(m):
    i, j = map(int, input().split())
    while True:
        if(i>=j): 
            break
        a[i-1], a[j-1] = a[j-1], a[i-1]
        i+=1
        j-=1
