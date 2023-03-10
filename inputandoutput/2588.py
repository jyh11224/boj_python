# 백준 2588번 문제
# 문제링크>> https://www.acmicpc.net/problem/2588
A= int(input())
B= int(input())

fir_remain = B % 10
sec_remain = (B // 10) % 10
thr_remain = (B // 10) // 10

print(A * fir_remain)
print(A * sec_remain)
print(A * thr_remain)
print(A * B)
