# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        mylist = []
        mylist = self.inorder(root, mylist)
        return self.construct(mylist)
        
            
    def inorder(self, node, mylist):
        if node.left:
            self.inorder(node.left, mylist)
        mylist.append(node)
        if node.right:
            self.inorder(node.right, mylist)
        return mylist
    
    def construct(self, mylist):
        if not mylist:
            return None
        mid = int(len(mylist)/2)
        root = mylist[mid]
        root.left = self.construct(mylist[:mid])
        root.right = self.construct(mylist[mid+1:])
        return root
