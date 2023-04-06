# 백준 2563번 문제
# 문제링크>> https://www.acmicpc.net/problem/2563
white_paper = [[0]*100 for i in range(100)]

count = int(input())
for i in range(count):
    left,right = map(int,input().split())
    for j in range(left,left+10):
        for k in range(right,right+10):
            white_paper[j][k] = 1
area = 0
for i in range(100):
    area += white_paper[i].count(1)
print(area)
