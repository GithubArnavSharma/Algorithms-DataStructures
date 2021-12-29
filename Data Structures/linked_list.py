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
  

N1 = Node(10)
N2 = Node(20)
N1.next_node = N2

l = LinkedList()
l.head = Node(10)
print(l.size())
