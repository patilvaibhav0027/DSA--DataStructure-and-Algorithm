queue = []

# 1. Enqueue Operation
def enqueue():
    element = input("Enter element: ")
    queue.append(element)
    print(element, "inserted into queue")


# 2. Dequeue Operation
def dequeue():
    if len(queue) == 0:
        print("Queue is Empty")
    else:
        element = queue.pop(0)
        print("Deleted element:", element)


# 3. Display Operation
def display():
    if len(queue) == 0:
        print("Queue is Empty")
    else:
        print("Queue elements:", queue)


# 4. Reverse Queue using Stack
def reverse_queue():
    if len(queue) == 0:
        print("Queue is Empty")
    else:
        stack = []

        while len(queue) > 0:
            stack.append(queue.pop(0))

        while len(stack) > 0:
            queue.append(stack.pop())

        print("Queue Reversed Successfully")


# 5. Merge Two Queues
def merge_queue():
    q2 = []

    n = int(input("Enter number of elements in second queue: "))

    for i in range(n):
        element = input("Enter element: ")
        q2.append(element)

    merged_queue = queue + q2

    print("First Queue:", queue)
    print("Second Queue:", q2)
    print("Merged Queue:", merged_queue)


# 6. Check Identical Queues
def identical_queue():
    q2 = []

    n = int(input("Enter number of elements in second queue: "))

    for i in range(n):
        element = input("Enter element: ")
        q2.append(element)

    if queue == q2:
        print("Both Queues are Identical")
    else:
        print("Both Queues are Not Identical")


# Main Menu
while True:

    print("\n----- LINEAR QUEUE OPERATIONS -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue using Stack")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        reverse_queue()

    elif choice == 5:
        merge_queue()

    elif choice == 6:
        identical_queue()

    elif choice == 7:
        print("Program Exited")
        break

    else:
        print("Invalid Choice")