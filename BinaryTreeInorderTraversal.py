# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        mylist = []
        self.Inordertravese(root, mylist)
        return mylist
    
    def Inordertravese(self, node, mylist):
        if node.left != None:
            self.Inordertravese(node.left, mylist)
  
        mylist.append(node.val)

        if node.right != None:
            self.Inordertravese(node.right, mylist)

        return mylist
