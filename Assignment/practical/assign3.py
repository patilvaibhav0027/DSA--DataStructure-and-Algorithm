# 18th November 2026
#

class node:
  def __init__(self, pid, name, pr):
    self.pid = pid
    self.name = name
    self.priority = pr
    self.next = None

class PriorityQueue:
  def __init__(self):
    self.front = self.rear = None

  #Add Process 
  def enqueue(self, new_node):
    if self.front == None:  # First node add inserted
      self.front = new_node
      return
    if self.front.priority > new_node.priority:  # Insert - first position
      new_node.next = self.front
      self.front = new_node
      return
    else:
      temp = self.front
      while temp:
        if new_node.priority < temp.priority:  
          break
        else:
          prev = temp
          temp = temp.next
      prev.next = new_node
      new_node.next = temp

  #Execute Process
  def dequeue(self):
    if self.front:
      temp = self.front
      print(f"Executed Process -> ID: {temp.pid}, Name: {temp.name}, Priority: {temp.priority}")
      self.front = self.front.next
    else:
      print("No pending processes in queue")

  #View Next Process
  def display_next(self):
    if self.front:
      print(f"Next Process -> ID: {self.front.pid}, Name: {self.front.name}, Priority: {self.front.priority}")
    else:
      print("No pending processes in queue")

  #  Display Processes
  def display_all(self):
    if self.front == None:
      print("No pending processes in queue")
      return
    temp = self.front
    print("Pending Processes:")
    while temp:
      print(f"[ID: {temp.pid} | Name: {temp.name} | Priority: {temp.priority}]")
      temp = temp.next

  # 5. Count Processes
  def count(self):
    temp = self.front
    total = 0
    while temp:
      total += 1
      temp = temp.next
    print("Total pending processes:", total)



pq = PriorityQueue()

pq.enqueue(node(101, "Chrome Browser", 2))
pq.enqueue(node(102, "Antivirus Scan", 3))
pq.enqueue(node(103, "Kernel Update", 1))
pq.enqueue(node(104, "Disk Cleanup", 4))
pq.enqueue(node(105, "Keyboard Input", 2))

pq.display_all()
print()
pq.count()
pq.display_next()
print()
pq.dequeue()
pq.dequeue()
print()
pq.display_all()
pq.count()