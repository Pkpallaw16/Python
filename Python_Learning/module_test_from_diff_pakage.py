import sys
print(sys.path)
sys.path.append(r'/module_implementation')
print(sys.path)
import mod
from mod import foo
print(mod.a)
foo(10)
obj=mod.Foo()
s="abc"
for i in range(len(s)):
    char = s[i:i + 1]
    s1 = s[:i] + s[i + 1:]
    print(s1)

a=[[1,2,3],[4,5,6],[6,7,8]]
b=[x[:1] for x in a]
print(max(b)[0])

