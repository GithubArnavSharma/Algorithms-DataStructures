class Node:
  """
  An object for storing a single node in a linked list
  Models the data of the node and the link to the next node in the list
  """
  
  data = None
  next_node = None
  
  def __init__(self, data):
    self.data = data
    
  def __repr__(self):
    return "<Node data: %s>" % self.data
  
class LinkedList:
  """
  Singly linked list
  """
  
  def __init__(self):
    self.head = None
    
  def is_empty(self):
    return self.head == None
  
  def size(self):
    current = self.head
    count = 0
    
    while current is not None:
      count += 1
      current = current.next_node
      
    return count
  
  def add(self, data):
    """
    Prepends a new node with data 'data' to the head of the list
    Time Complexity: O(1)
    """
    
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node
    
  def search(self, key):
    """
    Returns the node in the linked list with the data of key
    Time Complexity: O(n)
    """
    
    current = self.head
    
    while current:
      if current.data == key:
        return current
      current = current.next_node
     
    return None
  
  def insert(self, data, index):
    """
    Inserts a node with the value of data into index position of the linked list
    Finding index: O(n)
    Insertion: O(1)
    """
    
    node = Node(data)
    
    right_node = self.head
    left_node = None
    for i in range(index):
      left_node = right_node
      right_node = right_node.next_node
    
    if left_node is not None:
      left_node.next_node = node
    else:
      self.head = node

    node.next_node = right_node
    if right_node is None:
      self.tail = node
      
  def remove(self, key):
    current = self.head
    previous = None
    found = False
    
    while current is not None and not found:
      if current.data == key:
        found = True
      else:
        previous = current
      current = current.next_node
        
    if previous is None:
      self.head = current
    else:
      previous.next_node = current
      if current is None:
        self.tail = previous
    
  def __repr__(self):
    """
    Returns a string representing the list
    Time Complexity: O(n)
    """
    
    nodes = []
    current = self.head
    
    while current is not None:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.next_node is None:
        nodes.append("[Tail: %s]" % current.data)
      else:
        nodes.append("[%s]" % current.data)
      
      current = current.next_node
      
    return " -> ".join(nodes)
    
  
N1 = Node(10)
N2 = Node(20)
N1.next_node = N2

l = LinkedList()
l.head = Node(10)
print(l.size())

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l.size())
print(l)
print(l.search(1))
l.insert(4, 0)
l.insert(0, 4)
print(l)
l.remove(4)
l.remove(0)
print(l)
