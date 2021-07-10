num=[7,8,9,10]
it =iter(num)
print(it.__next__())
print(next(it))

class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num +=1
            return val
        else:
            raise StopIteration
values=topten()
for i in values:
    print(i)


class Test:

    # Cosntructor
    def __init__(self, limit):
        self.limit = limit

        # Called when iteration is initialized

    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

            # Else increment and return old value
        self.x = x + 1;
        return x

    # Prints numbers from 10 to 15


for i in Test(15):
    print(i)

# Prints nothing
for i in Test(5):
    print(i)
