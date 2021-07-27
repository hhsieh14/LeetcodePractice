#time complexity: O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            currentNode = root
            mylist = []
            queue = deque()
            queue.append(currentNode)
            while len(queue)>0:
                level_result = []
                for i in range(len(queue)):
                    currentNode = queue.popleft()
                    level_result.append(currentNode.val)
                    if currentNode.left != None:
                        queue.append(currentNode.left)
                    if currentNode.right != None:
                        queue.append(currentNode.right)
                mylist.append(level_result)
            return mylist
        else:
            return []
        
