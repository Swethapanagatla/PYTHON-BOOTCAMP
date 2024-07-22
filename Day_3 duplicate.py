n=list(map(int,input().split(" ")))
n1=[]
n2=[]
for i in n:
    if(i not in n1):
          n1.append(i)#removing duplicates
    else:
          n2.append(i)#printing duplicates
print(n1)
print(n2)
