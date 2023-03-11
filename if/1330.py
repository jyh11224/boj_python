# 백준 1330번 문제
# 문제링크>> https://www.acmicpc.net/problem/1330
A, B = map(int, input().split())

if(A>B):
    print(">")
elif(A<B):
    print("<")
elif(A==B):
    print("==")
