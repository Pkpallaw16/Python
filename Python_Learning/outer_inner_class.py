class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno,self.lap.show())

    class laptop:
        def __init__(self):
            self.brand="lenovo"
            self.cpu="I5"
            self.ram="8GB"
        def show(self):
            print(self.brand ,self.cpu ,self.ram)

s1=student("Aman",2)
s2=student("jai",3)
s1.show()
s2.show()


# Python program to demonstrate
# inner class


class person:
    def __init__(self):
        self.name = 'AKASH'
        self.db = self.Dob()

    def display(self):
        print('NAME = ', self.name)

        # this is inner class

    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 3
            self.yy = 2000

        def display(self):
            print('DOB = {}/{}/{}'.format(self.dd, self.mm, self.yy))

        # creating person class object


p = person()
p.display()

# create inner class object
x = p.db
x.display()


class person:
    def __init__(self):
        self.name = 'AKASH'
        self.db = self.Dob()

    def display(self):
        print('NAME = ', self.name)

        # this is inner class

    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 3
            self.yy = 2000

        def display(self):
            print('DOB = {}/{}/{}'.format(self.dd, self.mm, self.yy))

        # creating person class object


p = person()
p.display()

# create inner class object
x = p.db
x.display()
