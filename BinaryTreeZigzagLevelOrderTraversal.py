# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            currentNode = root
            mylist = []
            queue = deque()
            queue.append(currentNode)
            count = 0
            while len(queue)>0:#O(log(n))
                level_result = []
                for i in range(len(queue)):
                    currentNode = queue.popleft()
                    level_result.append(currentNode.val)
                    if currentNode.left != None:
                        queue.append(currentNode.left)
                    if currentNode.right != None:
                        queue.append(currentNode.right)
                if count % 2 != 0:
                    level_result.reverse()#O(l)
                mylist.append(level_result)
                count += 1
            return mylist
        else:
            return []
#O(log(n)/2 * (1+l))
