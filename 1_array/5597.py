# 백준 5597번 문제
# 문제링크>> https://www.acmicpc.net/problem/5597
n = [i for i in range(1, 31)]

for k in range(28):
    student = int(input())
    n.remove(student)

print(min(n))
print(max(n))
