class Myclass:
    def add(a,b):
        return(a+b)
    def sub(a,b):
        return(a-b)
    def mul(a,b):
        return(a*b)
    def div(a,b):
        return(a//b)
    def mod(a,b):
        return(a%b)
obj1=Myclass
obj2=Myclass
print(obj1.add(2,5))
print(obj1.sub(2,5)) 
print(obj2.mul(3,7))
print(obj2.div(21,7))
print(obj1.mod(5,2))
print(obj2.mod(15,5))