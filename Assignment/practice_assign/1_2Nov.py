# Q. 1 Create a Stack with following operations
# 1. Push
# 2. Pop
# 3. Display
# 4. Reverse String using Stack
# 5. Reverse Stack using another Stack

stack = []

# 1. Push Operation
def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(element, "pushed into stack")


# 2. Pop Operation
def pop():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        element = stack.pop()
        print("Popped element:", element)


# 3. Display Operation
def display():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Stack elements (Top to Bottom):")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])


# 4. Reverse String using Stack
def reverse_string():
    string = input("Enter a string: ")
    temp = []

    for ch in string:
        temp.append(ch)

    reverse = ""
    while len(temp) > 0:
        reverse += temp.pop()

    print("Reversed String:", reverse)


# 5. Reverse Stack using Another Stack
def reverse_stack():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        temp = []

        while len(stack) > 0:
            temp.append(stack.pop())

        while len(temp) > 0:
            stack.append(temp.pop())

        print("Stack Reversed Successfully")


# Main Menu
while True:
    print("\n----- STACK OPERATIONS -----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String using Stack")
    print("5. Reverse Stack using Another Stack")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        display()

    elif choice == 4:
        reverse_string()

    elif choice == 5:
        reverse_stack()

    elif choice == 6:
        print("Program Exited")
        break

    else:
        print("Invalid Choice")