# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return root
        q = deque([(root,0)])
        table = {}
        min_column = 0
        while q:
            node, column = q.popleft()
            if column < min_column:
                min_column = column
                
            if column not in table:
                table[column] = [node.val, ]
            else:
                table[column].append(node.val)
                
            if node.left:
                q.append((node.left, column - 1))
            if node.right:
                q.append((node.right, column + 1))
        output = []
        
        for i in range(len(table)):
            output.append(table[min_column])
            min_column += 1
        return output
