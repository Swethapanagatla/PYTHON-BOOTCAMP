#write a program to print all th prime numbers in a given range
n=int(input())
n1=int(input())
for i in range(n,n1+1):
    for j in range(2,i):
      if (i%j==0):
         break
    else:
       print(i)



