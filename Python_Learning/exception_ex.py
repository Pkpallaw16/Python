# class Error is derived from super class Exception
class Error(Exception):
    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass


class MarriageAge(Error):

    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, age, msg):
        self.age = age

        # Error message thrown is saved in msg
        self.msg = msg

    def print_info(self):
        print(self.age, self.msg)


try:
    age = int(input("enter age"))
    if age < 18 or age > 60:
        raise (MarriageAge(age, "Not Allowed"))
    else:
        Tr = MarriageAge(age, "Allowed")


# Value of Exception is stored in error
except MarriageAge as error:
    print('Exception occured: ', error.msg)
    age = int(input("enter correct age"))
    Tr = MarriageAge(age, "Allowed")


Tr.print_info()

