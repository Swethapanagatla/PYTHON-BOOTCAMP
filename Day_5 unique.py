#print the unique characters in a string
n=input()
n1=""
for i in n:
    if i not in n1:
        n1+=i
print(n1)

