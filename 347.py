class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        table = {}
        h = []
        for i in nums:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1
                
        for key, value in table.items():
            heapq.heappush(h,(value, key)) #nlogn
            
        tuples = heapq.nlargest(k,h)
        result = []
        
        for pair in tuples:
            result.append(pair[1])
        
        return result
