n=int(input())
count=0
for i in range(2,n//2+1):
    if(n%i==0):
        count+=1
        break
if (count==0 and n>1):
    print("num is prime") 
else:
    print("num not a prime")