class Solution(object):
    from collections import deque
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        root = (0,0)
        target = (x,y)
        visited = set()
        current = root
        q = deque()
        q.append(root)
        steps = 0
        while q:
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                if node == target:
                    return steps
                for action in offsets:
                    nextx, nexty = node[0]+action[0], node[1] + action[1]
                    if (nextx,nexty) not in visited:
                        visited.add((nextx,nexty))
                        q.append((nextx,nexty))
            steps += 1
            
        return steps
      
"""
Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
"""
