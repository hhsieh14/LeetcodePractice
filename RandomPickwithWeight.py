class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.Prefix_sums = []
        counter = 0
        for i in w:
            counter += i
            self.Prefix_sums.append(counter)
        self.total_sum = self.Prefix_sums[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        l , r = (0, len(self.w) - 1)
        while l < r:
            mid = int((r+l)/2)
            if target > self.Prefix_sums[mid]:
                l = mid + 1
            else:
                r = mid
        
        return r
