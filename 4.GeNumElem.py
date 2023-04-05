# Given a circular queue with max size = M to save each element, after several times enqueue (insert) & dequeue(delete) operations, front & rear have their own values, write a function or method getNumElem(size, front, rear) to find how many elements are in the circular queue 

def getNumElem(size, front, rear):
    if front == -1 and rear == -1:
        return 0
    elif front <= rear:
        return rear - front + 1
    else:
        return size - front + rear + 1

size = int(input("Please enter the size of the queue: "))
front = int(input("Please enter an number for the front of the queue: "))
rear = int(input("Please enter an number for the rear of the queue: "))
print(getNumElem(size, front, rear))

