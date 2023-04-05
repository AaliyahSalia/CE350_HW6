# Priority Queue is a queue with following properties

# a.	Every item has a priority associated with it.
# b.	In pop operation, an element with high priority will be dequeued (deleted) before an element with low priority.
# c.	If two elements have the same priority, they are served according to their order in the queue.

#For example, each element in a given queue is char type and priority of each element 		is ASCII code value, write functions to complete push and pop operations 
 

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def push(self, char):
        priority = ord(char)
        added = False

        for i in range(len(self.queue)):
            if priority > self.queue[i][1]:
                self.queue.insert(i, (char, priority))
                added = True
                break
        if not added:
            self.queue.append((char, priority))
    
    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[0]
    
    def is_empty(self):
        return len(self.queue) == 0

queue = PriorityQueue()
queue.push('C')
queue.push('O')
queue.push('D')
queue.push('A')


while not queue.is_empty():
    print(queue.pop(), end=' ')
