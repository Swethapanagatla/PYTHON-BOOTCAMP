my_list=[1, 2 ,3 ,4,4,2,3]
my_list2=[2,3,4,5]
my_list.append(99)
my_list.insert(2,99)
print(*my_list)# to print without braces and commas
print(len(my_list))
my_list.pop(0)
print(my_list)
newlist=my_list+my_list2
print(newlist)
new_list=my_list.copy()
new_list.append(8)
print(my_list)
print(my_list.count(2))
print(len(my_list))
my_list.sort()
print(*my_list)
li=list(map(int,input().split(" ")))
print(*li)