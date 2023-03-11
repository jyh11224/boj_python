# 백준 9498번 문제
# 문제링크>> https://www.acmicpc.net/problem/9498
A= int(input())

if(A>=90 and A<=100):
    print("A")
elif(A>=80 and A<=89):
    print("B")
elif(A>=70 and A<=79):
    print("C")
elif(A>=60 and A<=69):
    print("D")
else:
    print("F")
