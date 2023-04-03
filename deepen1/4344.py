# 백준 4344번 문제
# 문제링크>> https://www.acmicpc.net/problem/4344
i = int(input())
result = []
for j in range(i):
    sum = 0
    count = 0
    student = list(map(int, input().split()))
    for k in range(1, len(student)):
        sum += student[k]
        average = sum / (len(student) - 1)
    for k in range(1, len(student)):    
        if(student[k]>average):
            count += 1
    result.append(count/(len(student)-1)*100)
for a in result:
    print('%.3f'%(round(a, 3))+'%')
