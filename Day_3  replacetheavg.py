n=list(map(int,input().split(" ")))
max=n[0]
min=n[0]
for i in range(len(n)):
    if(n[i]>max):
      max=n[i]
for i in range(len(n)):
    if(n[i]<min):
      min=n[i]  
avg=(max+min)//2 
for i in range(len(n)):
    n[i]=avg
    print(n[i],end=" ")

