#single inheritance:
class Animal:
    def speak():
        return "animal is speaking"
class Dog(Animal):
    def bark():
        return "bow"
obj1=Animal
obj2=Dog
print(obj2.speak(),obj2.bark())
#multi level inheritance:
class Animal:
    def speak():
        return "animal is speaking"
class Dog(Animal):
    def bark():
        return "bow"
class Puppy(Dog):
    def speaking():
        return "i am puppy"
obj1=Animal
obj2=Dog
obj3=Puppy
print(obj3.speak(),obj3.bark(),obj3.speaking())
# multiple inheritance:
class Father:
    def speak():
        return "father class"
class Mother:
    def speaking():
        return "mother class"
class Kid(Father,Mother):
    def talk():
        return "i am kid "
obj1=Father
obj2=Mother
obj3=Kid
print(obj3.speak(),obj3.speaking(),obj3.talk())
