n=list(map(int,input().split(" ")))
even_sum=0
for i in range(0,len(n)):
    if n[i]%2==0:
        even_sum+=n[i]
even_avg=even_sum/len(n)
print(even_avg)