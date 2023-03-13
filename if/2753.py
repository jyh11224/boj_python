# 백준 2753번 문제
# 문제링크>> https://www.acmicpc.net/problem/2753
year = int(input())

four = year%4
beak = year%100
beak4 = year%400

if(four == 0 and beak != 0 or beak4 == 0):
    print("1")
else:
    print("0")
