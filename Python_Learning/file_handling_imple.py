f=open('sample_file.txt', 'r')
print(f.readline(),end=" ")
print(f.readline())

file = open("sample_file.txt", "r")
print(file.read())

# Writing to a file

f1= open ('mydata.txt', 'w')
f1.write('something')
f1.write('people')

file = open('mydata.txt', 'a')
file.write("This will add this line")
file.close()

#reading from one file and write to another file

f2=open('sample_file.txt', 'r')
f3=open ('mydata1.txt', 'w')
for data in f2:
    f3.write(data)

#It is designed to provide much cleaner syntax and exceptions handling when you are working with code. That explains why it’s
#good practice to use them with a statement where applicable.
#This is helpful because using this method any files opened will be closed automatically after one is done, so auto-cleanup.
with open("mydata.txt") as file:
    data = file.read()
    print(data)

with open("mydata.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)