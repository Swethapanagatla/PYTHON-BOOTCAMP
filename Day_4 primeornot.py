n=int(input())
c=0
if n<2:
    print("neither prime or composite")
else:
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
           c+=1
    if(c==1):
        print("prime")
    else:
        print("not prime")