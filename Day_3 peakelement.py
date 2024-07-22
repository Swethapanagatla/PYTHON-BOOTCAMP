arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        print(arr[i],end=" ")