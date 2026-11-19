class Node:
    def __init__(self, value):
        self.prev=None
        self.data=value
        self.next=None
class DLL:
    def __init__(self):
        self.head=None

    
    def append(self, new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head=new_node
        else:
            p = 1
            temp = self.head
            while p!=pos-1 and temp.next:
                temp = temp.next
                p += 1
            if temp.next: #last position
               temp.next.prev=new_node
            new_node.prev=temp
            new_node.next = temp.next
            temp.next = new_node   
            

    def delete(self, value):
        temp = self.head
        if temp == None:
            print("List is empty")
            return
        if temp.data == value:  # Delete the first node
            self.head = self.head.next
            return
        prev = temp
        temp = temp.next
        while temp != None and temp.data != value:
            prev = temp
            temp = temp.next
        if temp == None:
            print("Value is not present in the list")
            return
        prev.next = temp.next
        temp = None

    def reverse(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        self.head=prev

    def findmid_del(self):
        temp = temp1 = self.head
        prev=None
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        print("Middle Node: ",temp.data)
        prev.next=temp.next
        temp=None

    def del_first_last(self):
        temp1=self.head
        temp1=None
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next
        print()

list1 = DLL()
n1 = Node(10)
n2 = Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))
list1.print()
list1.insert(Node(34),1)
list1.print()
list1.insert(Node(60),6)
list1.print()