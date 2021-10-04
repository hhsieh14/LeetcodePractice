class Solution(object):
    import random
    from collections import defaultdict
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.table = defaultdict(list)
        for i , num in enumerate(nums):
            self.table[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = len(self.table[target]) * random.random()
        return self.table[target][int(index)]
