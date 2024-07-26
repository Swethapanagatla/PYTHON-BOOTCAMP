#hello-------wor-----ld=input
#------------helloworld=output
n=input()
c=0
s=" "
for i in n:
    if(i=='-'):
        c+=1
    else:
        s+=i
print("-"*c+s)
print("-"*c,s)
