import re
a="this is learnbay class1 class"
mobj=re.match("this",a)
print(mobj.group())

mobj1=re.match("learnbay",a)
#print(mobj1.group())

mobj1=re.search("(learnbay) (class)",a)
print(mobj1.group())

mobj1=re.search("(learnbay) (class)",a)
print(mobj1.group())
print(mobj1.group(1))

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("Phone Num : ", num)

op=re.sub("class","CLASS",a,count=2)
print(op)

b="this is learnbay class1 class2 class3"
op=re.findall("class",b,re.I)
print(op)

A="ABCDE123@#$^@123"
obj=re.search("\w",A)
sobj=re.search("\w+",A)
if obj:
    print(obj.group())
    print(sobj.group())
sobj=re.search("(\w+)(\W+)(\w+)",A)
if sobj:
    print(sobj.group())
    print(sobj.groups())

a="111111111"
obj=re.search("\d{4}",a)
sobj=re.search("\d{4,}",a)
print(obj.group())
print(sobj.group())

obj=re.search("[0-9]{4,6}",a)
print(obj.group())

a="111222222333"
obj=re.search("2{2,6}",a)
print(obj.group())

a="This is LEAR\nbay"
obj=re.search("lear.bay",a,re.I|re.S)
print(obj.group())


