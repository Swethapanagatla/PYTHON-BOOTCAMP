n=int(input())
n1=int(input())
for i in range(n,n1+1):
    for j in range(2,int(i**0.5)+1):
      if (i%j==0):
         break
    else:
       print(i)
