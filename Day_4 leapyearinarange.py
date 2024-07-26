n=int(input())
n1=int(input())
for i in (n,n1):
    if(i%4==0 and i%100!=0) or i%400==0:
       print(i)