"""R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):
    a =input().split()
    b=[]
    for j in range(C):
         b.append(int(a[j]))
    matrix.append(b)
print(matrix)

print(matrix[0:1][:])"""

import numpy as np
a=np.array([[2,3,4,5],[8,9,10,9],[1,6,7,9],[18,19,10,19]])
print(a[:,:])
print(a[0:3,0:1])
print(a[::-1,::-1])

cnt=1
for row in a:
    row[cnt:]=0
    cnt +=1
print(a)
cnt=1
for row in a:
    row[:cnt-1]=0
    cnt +=1
print(a)

m=np.random.randint(0,90,60).reshape(10,6)
print(m)
idx=np.where(m<30)
print(m[idx])
print(m[idx].size)
print(m[m<30])
