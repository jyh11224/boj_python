# 백준 2444번 문제
# 문제링크>> https://www.acmicpc.net/problem/2444
n = int(input())

for i in range(1,n):
    print((n-i)*" "+"*"*(2*i-1))
for i in range(n,0,-1):
    print((n-i)*" "+"*"*(2*i-1))
