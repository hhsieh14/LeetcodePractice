
class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here


def reverse(head):
  # Write your code here
  #dummy = Node(0)
  from collections import deque
  Q = deque()
  node = head
  
  while node != None:
    if node.data % 2 == 0:
      Q.append(node)
    if node.data % 2 != 0 or node.next == None:
      while Q:
        Q[0].data, Q[-1].data = Q[-1].data, Q[0].data
        Q.popleft() 
        if Q:
          Q.pop()
      
    node = node.next
  return head
