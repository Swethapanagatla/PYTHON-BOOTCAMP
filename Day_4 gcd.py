a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
while b!=0:
    a,b=b,a%b
print("gcd of the numbers is:",a)