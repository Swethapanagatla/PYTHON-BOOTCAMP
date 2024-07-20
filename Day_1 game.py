x_h=int(input())
x_w=int(input())
y_h=int(input())
y_w=int(input())
n=50//100*14
if(x_h==140 and x_w%2==0) and (y_h>118 and y_h<148) and y_w%7==0:
    print("x y z on same plane")
else:
    print("no")