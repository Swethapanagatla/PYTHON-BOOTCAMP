n=input()
n3=n.lower()
n1="aeiou"
a="bcdfghjklmnpqrstvwxyz"
c=0
c1=0
for i in n3:
    if i in n1:
      c+=1
print(c)
for i in n3:
    if i in a:
       c1+=1
print(c1)

 
