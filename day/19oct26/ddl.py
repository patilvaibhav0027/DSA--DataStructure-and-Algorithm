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
        temp=self.head
        if temp.data==value: #first node
            self.head=self.head.next
            self.head.prev=None
        else:
            while temp.data!=value and temp:
                temp=temp.next
                if temp==None:
                    print("Value not present")
                    return
            temp.prev.next=temp.next
            if temp.next: # not last node
                temp.next.prev=temp.prev
            temp=None

    def printrev(self):
        temp=self.head
        print('\n List Element in reversse order:', end = "")
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data, end="")
            temp = temp.prev

    # def findmid_del(self):
    #     temp = temp1 = self.head
    #     prev=None
    #     while temp1 and temp1.next:
    #         prev=temp
    #         temp=temp.next
    #         temp1=temp1.next.next
    #     print("Middle Node: ",temp.data)
    #     prev.next=temp.next
    #     temp=None

    # def del_first_last(self):
    #     temp1=self.head
    #     temp1=None
    #     prev=None
    #     temp=self.head=self.head.next
    #     while(temp.next):
    #         prev=temp
    #         temp=temp.next
    #     prev.next=None

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

print("revsered list")x
list1.printrev()

# list1.insert(Node(2),2)
# list1.print()
# list1.delete(2)
# list1.print()
# list1.delete(3)
# list1.print()
# print("Reversed LL:")
# list1.reverse()
# list1.print()
# list1.findmid_del()
# list1.print()
# list1.del_first_last()
# list1.print()