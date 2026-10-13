#linked list5
#09/10/2026


# Singly Linear Linked List - Insert at Position

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head

            while p != pos - 1:
                temp = temp.next
                p += 1

            new_node.next = temp.next
            temp.next = new_node

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


list1 = SLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

list1.insert(Node(25), 3)

list1.print_list()