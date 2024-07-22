n=int(input())
temp=n
sum=0
while(temp>0):
    rem=temp%10
    sum+=rem**2
    temp=temp//10
print(sum)