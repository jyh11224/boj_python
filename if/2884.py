# 백준 2884번 문제
# 문제링크>> https://www.acmicpc.net/problem/2884
h,m= map(int,input().split())
if m<45: 
   if h == 0:
      h = 23
      m += 60
   else:
      h -=1
      m += 60
print(h,m-45)
