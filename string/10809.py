# 백준 10809번 문제
# 문제링크>> https://www.acmicpc.net/problem/10809
str = input()
alphabet = 97
sw = 0
for i in range(26):
    for j in range(len(str)):
        if(chr(alphabet) == str[j]):
            print(j)
            sw = 1
            break
    alphabet +=1
    if(sw == 0): print(-1)
    sw = 0
