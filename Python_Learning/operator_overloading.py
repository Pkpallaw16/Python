class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        #return '{} {} .format(self.m1,self.m2)'
        return 's1(m1=' + str(self.m1) + ', m2=' + str(self.m2) + ')'
        #return self.m1, self.m2


s1=student(90,95)
s2=student(70,80)
s3=s1+s2
print(s3.m1,s3.m2)

if s1>s2:
    print("S1 wins")
else:
    print("s2 wins")
print(s3)

a=9
print(a.__str__())

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        # adding two objects

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __str__(self):
        return self.a, self.b


Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)


class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if (self.a < other.a):
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if (self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"


ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2) 