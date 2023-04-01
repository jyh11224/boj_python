# 백준 3003번 문제
# 문제링크>> https://www.acmicpc.net/problem/3003
chess = [1, 1, 2, 2, 2, 8]
a = list(map(int, input().split()))

for i in range(len(chess)):
    if(a[i] == chess[i]):
        print(0,end=" ")
    else:
        print(chess[i] - a[i], end=" ")
