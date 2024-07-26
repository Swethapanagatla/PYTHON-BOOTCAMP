#method overriding:same method print last method by method overriding
class Animal:
    def speak():
        return "animal is speaking"
class Dog(Animal):
    def speak():
        return "bow"
class Puppy(Dog):
    def speak():
        return "i am puppy"
obj1=Puppy
print(obj1.speak())
