"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        mylist = []
        mylist = self.inorder(root, mylist)
        head = mylist[0]
        for i, node in enumerate(mylist):
            #print(node.val)
            if i == 0:
                node.left = mylist[-1]
            else:
                node.left = mylist[i - 1]
            if i == len(mylist) - 1:
                node.right = mylist[0]
            else:
                node.right = mylist[i + 1]
            
        return head
    
    def inorder(self, node, mylist):
        
        if node.left:
            self.inorder(node.left, mylist)
            
        mylist.append(node)
        
        if node.right:
            self.inorder(node.right, mylist)
        return mylist
