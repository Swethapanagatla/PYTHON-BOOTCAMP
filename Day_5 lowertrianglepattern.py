n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print( )



n=int(input())
for i in range(n):
    for j in range(n):
        if (i<=j):
           print("*",end=" ")
    print( )