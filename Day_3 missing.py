n=int(input())
sum=n*(n+1)//2
n1=list(map(int,input().split(" ")))
sum1=0
for i in range(len(n1)):
    sum1+=n1[i]
print(sum-sum1)