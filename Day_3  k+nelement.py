n=int(input())
k=int(input())
x=n+k
n1=list(map(int,input().split(" ")))
if(len(n1)<x):
    print("error")
else:
    for i in range (len(n1)):
        if(n1[i]==x):
            break
print(n1[i])