# 백준 2231번 문제
# 문제링크>> https://www.acmicpc.net/problem/2231

n = int(input())
result = 0
for i in range(1, n+1):
    nums = list(map(int, str(i)))
    result = sum(nums) + i
    if result == n:
        print(i)
        break
    if i == n:
        print(0)
