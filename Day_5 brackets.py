#remove all the brackets from the given algebric expression
n=input()
s=""
for i in n:
    if(ord(i)!=40 and ord(i)!=41 and ord(i)!=91 and ord(i)!=93 and ord(i)!=123 and ord(i)!=125):
          s+=i
print(s)
           
       