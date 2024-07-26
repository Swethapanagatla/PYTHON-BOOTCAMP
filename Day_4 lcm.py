#a=int(input("enter the 1st number"))
#b=int(input("enter the 2nd number"))
#while b!=0:
 #   a,b=b,a%b
#print("lcm of the numbers is:",a*b//a)#--->#this gives 0 because 
                                       # after the operations a and b 
                                        #are modified so b becomes 0 
                                        #in this case so try 
                                        #multiplying the a and b values 
                                       #before the loop and store it in a variable
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
x=a*b
while b!=0:
    a,b=b,a%b
print("lcm of the numbers is:",x//a)