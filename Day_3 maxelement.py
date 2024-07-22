n=list(map(int,input().split(" ")))
max=0
for i in range(len(n)):
    if(n[i]>max):
      max=n[i]
print(max)