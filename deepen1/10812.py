# 백준 10812번 문제
# 문제링크>> https://www.acmicpc.net/problem/10812
n, m = map(int, input().split()) 
basket = [a for a in range(1,n+1)]

for b in range(m):
    i,j,k = map(int, input().split())
    i,j,k = i-1, j-1, k-1
    basket = basket[:i] + basket[k:j+1] + basket[i:k] + basket[j+1:]
       

print(*basket)
