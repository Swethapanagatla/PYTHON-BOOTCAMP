li=list(map(int,input().split()))
print("press 1 for appending")
print("press 2 for poping")
print("press 3 for sort")
print("press 4 for len")
choice=int(input())
if choice==1:
    li.append(5)
    print(li)
elif choice==2:
    li.pop(2)  
    print(li) 
elif choice==3:
    li.sort() 
    print(li) 
else:
    a=len(li)
    print(f"hello len(li) is {a}")