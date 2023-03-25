# 백준 2562번 문제
# 문제링크>> https://www.acmicpc.net/problem/2562
str = []
for i in range(9):
    str.append(int(input()))
print(max(str), str.index(max(str))+1)
