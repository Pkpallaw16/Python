"""Python stack can be implemented using deque class from collections module. Deque is preferred over list in the cases where we need quicker
append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as
compared to list which provides O(n) time complexity. Same methods on deque as seen in list are used, append() and pop()."""
from collections import deque

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())


print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty 



stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)

# pop() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

#Queue_data structue module also has a LIFO Queue_data structue, which is basically a 5 Stack_data structure. Data is inserted into Queue_data structue using put() function and get()
#takes data out from the Queue_data structue. There are various functions available in this module:

from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())

