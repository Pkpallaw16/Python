try:
   f = open("test.txt",'r', encoding = 'utf-8')
   # perform file operations
except FileNotFoundError:
    f = open("test.txt", "w")
finally:
   f.close()