"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        a_p = []
        
        while p:
            if p:
                a_p.append(p)
                p = p.parent
        while q not in a_p:
            q = q.parent
        
        return q
