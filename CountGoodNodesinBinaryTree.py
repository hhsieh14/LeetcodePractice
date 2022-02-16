# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, mylist, maxval):
            nonlocal count
            
            mylist.append(node)
            if node.left != None:
                dfs(node.left, mylist, max(maxval, node.left.val))
            if node.right != None:
                dfs(node.right, mylist, max(maxval, node.right.val))
                 
            if node.val >= maxval:
                count += 1
                          
            return count
        
        mylist = []
        
        return (dfs(root, mylist, root.val))
