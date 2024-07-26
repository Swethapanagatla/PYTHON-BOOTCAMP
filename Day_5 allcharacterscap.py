#write a code to print all the characters in a given string
n=input()
s=""
for i in n:
    if (ord(i)>=60 and  ord(i)<=90):
        s+=i
print(s)