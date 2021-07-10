# a file named "geek", will be opened with the reading mode.
file = open('abc.txt', 'r')
# This will print every line one by one in the file
print(file.read(4))
print(file.read(13))
print(file.readline(14))
print(file.readlines())


