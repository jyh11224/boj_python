# 백준 1546번 문제
# 문제링크>> https://www.acmicpc.net/problem/1546
n = int(input())
a = list(map(int, input().split()))
new_score = []
sum = 0
for i in range(n):
    new_score.append(a[i]/max(a)*100)
    sum += new_score[i]
print(sum/n)  
