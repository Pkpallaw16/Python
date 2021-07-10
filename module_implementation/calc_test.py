import calc
#from calc import add, subtract,Audi
print(dir(calc))

from calc import *
print(calc.a)
print(calc.b)
print(calc.__name__)
print(__name__)

print(add(10, 2))
print(subtract(10, 2))

aud=Audi().outModels()



