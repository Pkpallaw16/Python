# Program to show various ways to
# read data from a file.

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Creating a file
with open("myfile.txt", "w") as file1:
   # Writing data to a file
   file1.write("Hello \n")
   file1.writelines(L)
   file1.write("at the end of file\n")

with open("myfile.txt", "r+") as file1:
   # Reading form a file
   print(file1.read())

with open("myfile.txt", "r") as file:
   data = file.readlines()
   for line in data:
      word = line.split()
      print (word)
# Python code to illustrate append() mode
file = open('myfile.txt','a')
file.write("This will add this line")
file.close()

