import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        h = []
        for pairs in points:
            dis =  pairs[0]**2 + pairs[1]**2
            heappush(h, (dis, pairs)) #O(logn)
        output = []
        for _ in range(k):
            next_item = heappop(h)#O(logn)
            output.append(next_item[1])#O(1)
        return output
    ##total time: O(nlogn + klogn), space: heap stores n elements output stores k elements --> O(n+k)
