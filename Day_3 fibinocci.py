n=int(input())
fib_series=[0,1]
for i in range(2,n):
    nxt=fib_series[-1]+fib_series[-2]
    fib_series.append(nxt)
print(fib_series[:n])