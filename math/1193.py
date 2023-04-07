# 백준 1193번 문제
# 문제링크>> https://www.acmicpc.net/problem/1193
x = int(input())
line = 1
while line<x:#1<8  27 35 42
    x -= line
    line +=1

if (line%2) == 0:
    n , m = x , line+1-x
else:
    n, m = line + 1 - x, x
print(n,'/',m, sep = '')
