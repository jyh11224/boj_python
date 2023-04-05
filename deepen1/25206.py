# 백준 25206번 문제
# 문제링크>> https://www.acmicpc.net/problem/25206
sum1 = 0
sum2 = 0
grade_list = [('A+', 4.5),('A0', 4.0),('B+', 3.5),('B0', 3.0),('C+', 2.5),('C0', 2.0),('D+', 1.5),('D0', 1.0),('F', 0.0)]

for i in range(20):
    info = list(input().split())
    for grade in grade_list:
        if(info[2]==grade[0]):
            sum1 += float(info[1])
            sum2 += float(grade[1]) * float(info[1])
        elif(info[2] == 'P'):
            continue
print(sum2 / sum1)
