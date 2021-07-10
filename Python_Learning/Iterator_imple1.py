class Remotecontrol:
    def __init__(self):
        self.channel=['HBO','cnn','starplus','sony','espn','max','colours']
        self.index=-1

    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index==len(self.channel):
            raise StopIteration
        else:
            return self.channel[self.index]

r=Remotecontrol()
itr=iter(r)
print(next(itr))
print(next(itr))
values=Remotecontrol()
for i in values:
    print(i)