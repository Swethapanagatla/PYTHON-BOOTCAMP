li=list(map(int,input().split(",")))
count=0
for i in range(1,len(li)+1):
     if(i%2==0):
         count+=1
print(count)          

