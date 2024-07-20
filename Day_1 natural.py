n=int(input())
n1=n
temp=0
while n1>0:
   rem=n1%10
   temp=temp*10+rem
   n1=n1//10
if(n==temp):
    print("palindrome")
else:
    print("not palindrome")
