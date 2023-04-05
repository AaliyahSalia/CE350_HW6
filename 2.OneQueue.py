#Create a function to simulate stack push & pop operations by using only ONE queue

from queue import Queue

class Stack:
    def __init__(self):
        self.q = Queue()

    def push(self, val):
        self.q.put(val)
        size = self.q.qsize()

        for i in range(size - 1):
            self.q.put(self.q.get())

    def pop(self):
        if self.q.empty():
            return None
        return self.q.get()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.pop())

