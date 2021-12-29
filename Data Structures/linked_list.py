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
