n=int(input())
count=0
if n==1:
    print("not a prime")

else:
    for i in range (1,n+1):
      if(n%i)==0:
        count+=1
if (count==2):
    print("prime")
else:
    print("not prime")