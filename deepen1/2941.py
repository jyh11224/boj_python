# 백준 2941번 문제
# 문제링크>> https://www.acmicpc.net/problem/2941
s = str(input())
a = ["c=","c-","dz=","d-","lj","nj","s=","z="]
sum1 = 0
sum2 = 0
for i in a:
    s = s.replace(i, '*')

print(len(s))
