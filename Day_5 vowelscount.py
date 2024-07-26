#check how many vowels are there in string
n=input()
n1=['a','e','i','o','u']
n3=n.lower()
c=0
for i in n3:
    if i in n1:
      c+=1
print(c)
 
