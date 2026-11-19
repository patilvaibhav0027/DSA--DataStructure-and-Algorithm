class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,new_node):
        new_node.next = self.top
        self.top=new_node

    def print(self):
        temp = self.top
        print("stack elements: ")
        while (temp):
            print(temp.data)
            temp=temp.next

class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    def dequeue(self):

        if self.front :
            temp = self.front
            dequed_data = temp.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
                print("now queue is empty")
            temp = None
            return dequed_data
        else:
            print("queue is empty")

    def is_empty(self):
        return self.front is None
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

def reverse_queue(q1):
    st1 = Stack()
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))
    st1.print()



# Create a queue
myQueue = LQueue()
myQueue.enqueue(11)
myQueue.enqueue(58)
myQueue.enqueue(22)
print("Queue: ", end="")
myQueue.printQueue()
reverse_queue(myQueue)
