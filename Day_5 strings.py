#strings methods are:
#1)isalpha
#2)isalum
#3)isupper
#4)islower
#5)lowercase
#6)uppercase
#7)titlecase
#8)swapcase
n="HELLaaaO   world"#HELLaaaaO    world
print(n.upper())#HELLAAAAO    WORLD
print(n.lower())#hellaaaao    world
print(n.title())#Hellaaaao    World--(only 1st letter of each word is capital)
print(n.capitalize())#hellaaaao    world
print(n.swapcase())#hellAAAAo    WORLD
print(n.strip())#HELLaaaaO    world --(remove front and last spaces)
print(n.replace('a','z'))# HELLzzzzO    world
print(n.split())#['HELLaaaaO', 'world']
print(n.split('a'))#['     HELL', '', '', '', 'O    world']
n="Hello"
print(n.isalpha())#true
print(n.isnumeric())#false
print(n.isalnum())#true
print(n.isascii())#true
print(n.isupper())#false
print(n.istitle())#true
print(n.isdigit())#false
