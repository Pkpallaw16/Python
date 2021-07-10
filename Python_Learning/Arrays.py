import array as arr
vals= arr.array('i',[7,8,9,10,11,3])
print(vals)
print(vals.buffer_info())
print(vals.typecode)
vals.reverse()
print(vals)

newarr=arr.array(vals.typecode,[i**2 for i in vals])
print(newarr)

# values from user
val= arr.array('i',[])
n=int(input("array size"))
for i in range(n):
    x=int(input("enter the next value"))
    val[i]=x
print(val)


