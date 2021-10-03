class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        from collections import deque
        
        q = deque()
        
        q.append(root)
        re = 0
        while q:
            node = q.popleft()
            if node.val <= high and node.val >= low:
                re += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return re
