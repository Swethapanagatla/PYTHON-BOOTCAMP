n=int(input())
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print( )


n=int(input())
for i in range(n):
    for j in range(n):
        if (i>=j):
           print("*",end=" ")
    print( )