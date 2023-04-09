# 백준 9506번 문제
# 문제링크>> https://www.acmicpc.net/problem/9506
while(True):
    n=int(input())
    list=[]
    result=0
    if n == -1 :
        break
    else :
        for i in range(1,n+1):
            if n%i==0:
                list.append(i) #list에 n의 약수를 추가.
    #list에서 약수들을 더해서 n이 나오면 완전수
    for i in range(len(list)-1):
        result+=list[i]
    if result==n:
        print(f"{result} = {list[0]}", end = ' ')
        for i in range(1, len(list)-1):
            print(f"+ {list[i]}", end = ' ')
        print()
    else :
        print(f'{n} is NOT perfect.')
