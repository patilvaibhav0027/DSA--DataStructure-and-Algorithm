# Ass1: Create a Singly Linear Linked List with following operations
# Create Linked List
# Traverse and print the node values
# Insert node at a specific position
# Find Middle node and print its value
# Delete node
# Reverse list
# Calculate the sum of every two consecutive node values.

#creating a node with data and next.
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

#creating a class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List 
    #function creation
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input(f"Enter value for node {i + 1}: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

        print("LL created successfully")

    # 2. Traverse and Print
    #function creation
    def traverse(self):
        if self.head is None:
            print("LL is empty.")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert at Specific Position
    #function creation
    def insert(self, data, position):
        new_node = Node(data)

        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position.")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position.")
            return

        new_node.next = temp.next
        temp.next = new_node
        print("Node inserted successfully")

    # 4. Find Middle Node
    #function creation
    def middle(self):
        if self.head is None:
            print("LL is empty.")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node value:", slow.data)

    # 5. Delete Node at Specific Position
    #function creation
    def delete(self, position):
        if self.head is None:
            print("LL is empty.")
            return

        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.head = self.head.next
            print("Node deleted successfully")
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position.")
                return
            temp = temp.next

        if temp is None or temp.next is None:
            print("Invalid position.")
            return

        temp.next = temp.next.next
        print("Node deleted successfully")

    # 6. Reverse Linked List
    #function creation
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
        print("LL reversed successfully")

    # 7. Sum of Every Two Consecutive Nodes
    #function creation

    def pair_sum(self):
        if self.head is None or self.head.next is None:
            print("At least two nodes are required.")
            return

        temp = self.head

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(f"{temp.data} + {temp.next.data} = {total}")
            temp = temp.next

# Main Program
ll = LinkedList() #ll: is object and LinkedList: is class

while True:
    print("1. Create LL")
    print("2. Traverse LL ")
    print("3. Insert Node")
    print("4. Find Middle Node")
    print("5. Delete Node")
    print("6. Reverse LL ")
    print("7. Sum of Two Consecutive Nodes")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ll.create()

    elif choice == 2:
        ll.traverse()

    elif choice == 3:
        data = int(input("Enter value to insert: "))
        position = int(input("Enter position: "))
        ll.insert(data, position)

    elif choice == 4:
        ll.middle()

    elif choice == 5:
        position = int(input("Enter position to delete: "))
        ll.delete(position)

    elif choice == 6:
        ll.reverse()

    elif choice == 7:
        ll.pair_sum()

    elif choice == 8:
        print("Program terminated")
        break

    else:
        print("Invalid choice please try again")
        print("LL created successfully")
