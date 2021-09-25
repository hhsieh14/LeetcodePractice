from collections import deque

# Add any helper functions you may need here


def minOperations(arr):
  # Write your code here
  fringe = deque()
  closed = []
  fringe.append((arr,0))
  while fringe:
    node,level = fringe.popleft()
    if goaltest(node):
      return level
    if node not in closed:
      expansion = expand(node, closed)
      for i in range(len(expansion)):
        fringe.append((expansion.pop(), level + 1) )
 


def expand(node, closed):
  i = 0
  j = 1
  expand = []
  for i in range(len(node) - 1):
    for j in range(1,len(node)):
      newnode = node[:i] + list(reversed(node[i:j + 1])) + node[j + 1:]
    if newnode not in closed:
      expand.append(newnode)
  return expand
  
  
def goaltest(node):
  return node == sorted(node)
