import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
            
        result = heapq.nlargest(k,nums) ##O(N + klogN)
        ##log N for finding max value
        ##k for the first k element
        ## N for heapify
        return result[-1]
