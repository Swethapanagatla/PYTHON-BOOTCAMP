#write a program to print all the vowels followed by consonents
n=input()
n3=n.lower()
n1="aeiou"
a="bcdfghjklmnpqrstvwxyz"
for i in n3:
    if i in n1:
      print(i,end=" ")
for i in n3:
    if i in a:
      print(i,end=" ")

 


 
