# 백준 5622번 문제
# 문제링크>> https://www.acmicpc.net/problem/5622
alpha_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

a = str(input())
sum = 0
for b in range(len(a)):
    for i in alpha_list:
        for j in i:
            if(a[b] == j):
                sum += (alpha_list.index(i) + 3)

print(sum)
