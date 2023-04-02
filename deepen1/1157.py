# 백준 1157번 문제
# 문제링크>> https://www.acmicpc.net/problem/1157
s = str(input().upper())
word_list = list(set(s))
cnt = []
for i in word_list:
    cnt.append(s.count(i))
count = 0

for i in cnt:
    if(i == max(cnt)):
        count+=1

if(count>=2):
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])
