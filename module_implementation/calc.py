# A simple module, calc.py
a=10
b=40
class Audi:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.models = ['q7', 'a6', 'a8', 'a3']

    # A normal print function
    def outModels(self):
        print('These are the available models for Audi')
        for model in self.models:
            print('\t%s ' % model)


def add(x, y):
	return (x+y)

def subtract(x, y):
	return (x-y)
if __name__== '__main__':
    print(add(2,3))
    print(subtract(4,1))
    a1=Audi()
    a1.outModels()