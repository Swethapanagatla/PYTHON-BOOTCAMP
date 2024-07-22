n=int(input())
rev=""
while(n>0):
    rem=n%10
    rev=rev+str(rem)
    n=n//10
print(rev)#type str
print(int(rev))#type integer