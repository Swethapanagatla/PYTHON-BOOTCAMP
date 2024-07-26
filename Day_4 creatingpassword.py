n=input("enter the password")
n1=len(n)
c=0
str="a/"
for i in n:
    if(i in str[0] or str[1] and i not in" "):
       c+=1
       break
if(c==0 or n1<8):
    print("follow the conditions")
elif(n1==8):
    print("password if weak")
elif(n1>=8 and n1<12):
    print("password is modrate")
elif(n1>=12 and n1<=15):
    print("password if strong")




       
