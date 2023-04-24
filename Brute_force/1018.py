# 백준 1018번 문제
# 문제링크>> https://www.acmicpc.net/problem/1018

n,m = map(int, input().split())
string = []
count = []

for _ in range(n):
    string.append(input())

for i in range(n-7):
    for j in range(m-7):
        index1 = 0
        index2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if ((a+b)% 2 == 0):
                    if(string[a][b] != 'W'):
                        index1 += 1
                    if(string[a][b] != 'B'):
                        index2 += 1
                else:
                    if(string[a][b] != 'B'):
                        index1 += 1
                    if(string[a][b] != 'W'):
                        index2 += 1
        count.append(min(index1,index2))
print(min(count))
