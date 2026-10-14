#14/10/2026
# singly ciruclar linked list
#insert at 1st position and last position


class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
class SCLL:
    def __init__(self):
        self.head=None
    
    def append(self, new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
        new_node.next=self.head

    # insert at first position
    def insert(self, new_node, pos):  
        if pos == 1:
            temp = self.head
            while temp.next != self.head:
                temp=temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next=self.head
        else:#insert node from 2nd to last position
            p = 1
            temp = self.head
            while (p != pos - 1 and temp.next != self.head):
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, value):
        temp = self.head
        if temp == None:
            print("List is empty")
            return
        if temp.data == value:  # Delete the first node
            while temp.next != self.head: #find the last node
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
        else:
            while (temp.data != value):
                prev = temp
                temp = temp.next
            if temp == self.head:
                print("Value is not present in the list")
                return 
        prev.next = temp.next
        temp = None

    def print(self):
        temp=self.head
        while(True):
            print(temp.data, end=" ")
            temp=temp.next
            if temp==self.head:
                break
        print()

list1 = SCLL()
n1 = Node(10)
n2 = Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))
list1.append(Node(65))
list1.print()
list1.insert(Node(58), 70)
list1.print()
list1.delete(50)
list1.print()