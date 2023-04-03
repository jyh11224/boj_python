# 백준 1316번 문제
# 문제링크>> https://www.acmicpc.net/problem/1316
num = int(input())
count = num
for i in range(num):
    j = str(input())
    for k in range(len(j)-1):
        if(j[k] != j[k+1]):
            if(j[k+1] in j[:k]):
                count -= 1    
                break
            
print(count)
