# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque()
        q.append(root)
        q.append(root)
        while (q):
            t1 = q.popleft()
            t2 = q.popleft()
            if t1 == None and t2 == None:
                continue
            elif t1 == None or t2 == None:
                return False
            elif t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True
###O(n)
