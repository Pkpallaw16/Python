import numpy as np
arr=np.array([1,2,3,4])
print(arr)
print(np.zeros(6))
print(np.ones(6))
print(np.linspace(0,15,16))
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
arr2=arr1.flatten()
print(arr2)
print(arr2.reshape(3,2))
m=np.matrix(arr1)
print(m)
print(np.arange(1,15,2))


m1= np.array([np.arange(0,3), np.arange(3,6)])
print(m1)
print("Sliced: n ", m1[:, 2:])
print("Transpose n ", m1.T)


## A = (3,3) matrix
A = np.array([[1, 1, 1], [2, 4, 1], [1, -1, 1]])
## B = (3,1) matrix
B = np.array([1, -2, 0]).T

## X = Inv(A).B = (3, 1) in shape
X = np.dot(np.linalg.inv(A), B)
print("Solution: n ", X)

print(np.zeros((3, 4)))
print(np.ones((3, 4)))
b = np.matrix('[1,2;3,4;5,6]')
print(b)
c = np.matrix(np.random.rand(3, 3), dtype=np.float32)
print(c)
result = np.matrix(np.zeros((2,2)))
print(result)
matA = np.matrix(np.random.rand(3, 2))
# get the inverse of the first matrix
inverseMatA = matA.getI()
print('\nThe inverse of the first matrix is :\n', inverseMatA)

# get the transpose matrix of the second matrix
transposeMatB = matA.getT()
print('\nThe transpose of the second matrix is :\n', transposeMatB)

# Find maximum element in each row
print(np.max(matA, axis=1))
# Find the mean value in each column
print(np.mean(arr1, axis=0))


# Create matrix
matrix = np.array([[1, 2, 3],
                   [2, 4, 6],
                   [3, 8, 9]])

# Return determinant of matrix
print(np.linalg.det(matrix))

vector_a = np.array([1,2,3])
vector_b = np.array([4,5,6])

# Calculate dot product
np.dot(vector_a, vector_b)


matrix_a = np.array([[1, 1],
                     [1, 2]])

# Create matrix
matrix_b = np.array([[1, 3],
                     [1, 2]])

# Multiply two matrices
np.dot(matrix_a, matrix_b)

# Draw three numbers from a normal distribution with mean 0.0
# and standard deviation of 1.0
np.random.normal(0.0, 1.0, 3)

# Draw three numbers from a logistic distribution with mean 0.0 and scale of 1.0
np.random.logistic(0.0, 1.0, 3)

# Draw three numbers greater than or equal to 1.0 and less than 2.0
np.random.uniform(1.0, 2.0, 3)

# Generate three random integers between 0 and 10
np.random.randint(0, 11, 3)

# Generate three random floats between 0.0 and 1.0
np.random.random(3)

# Set seed
np.random.seed(0)

# Multiply two matrices element-wise
matrix_a * matrix_b

# Create matrix
matrix = np.array([[1, -1, 3],
                   [1, 1, 6],
                   [3, 8, 9]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Return diagonal one above the main diagonal
matrix.diagonal(offset=1)

# Return diagonal one below the main diagonal
matrix.diagonal(offset=-1)

# Return diagonal elements
matrix.diagonal()

# Return matrix rank
np.linalg.matrix_rank(matrix)

#flatten is a simple method to transform a matrix into a one-dimensional array. Alternatively, we can use reshape to create a row vector:
#One useful argument in reshape is -1, which effectively means “as many as needed,” so reshape(1, -1) means one row and as many columns as needed:

matrix.reshape(1, -1)
