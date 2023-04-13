# 백준 5073번 문제
# 문제링크>> https://www.acmicpc.net/problem/5073
while(True):    
    a,b,c = map(int, input().split())
    if(a==0 and b==0 and c==0):
        break
    list=[a,b,c]
    if sum(list) <=max(list)*2:
        print("Invalid")
    elif(a == b and b == c and c==a):
        print("Equilateral")
    elif(a==b or b==c or c==a):
        print("Isosceles")
    else:
        print("Scalene")
