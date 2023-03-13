# 백준 14681번 문제
# 문제링크>> https://www.acmicpc.net/problem/14681
a = int(input())
b = int(input())

if(a>0 and b>0):
    print("1")
elif(a<0 and b>0):
    print("2")
elif(a<0 and b<0):
    print("3")
elif(a>0 and b<0):
    print("4")
