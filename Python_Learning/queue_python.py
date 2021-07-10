"""List is a Python’s built-in data structure that can be used as a queue. Instead of enqueue() and dequeue(), append() and pop() function is used.
However, lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all of the other elements
by one, requiring O(n) time."""

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue_data structue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty

"""Queue_data structue in Python can be implemented using deque class from the collections module. Deque is preferred over list in the cases where we need quicker append 
and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides
O(n) time complexity. Instead of enqueue and deque, append() and popleft() functions are used."""

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue_data structue after removing elements")
print(q)

# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty

#Queue_data structue is built-in module of Python which is used to implement a queue. queue.Queue_data structue(maxsize) initializes a variable to a maximum size of maxsize.
#A maxsize of zero ‘0’ means a infinite queue. This Queue_data structue follows FIFO rule.There are various functions available in this module:

from queue import Queue

# Initializing a queue
q = Queue(maxsize=3)

# qsize() give the maxsize
# of the Queue_data structue
print(q.qsize())

# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full
# Queue_data structue
print("\nFull: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty
# Queue_data structue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())

# This would result into Infinite
# Loop as the Queue_data structue is empty.
# print(q.get())

