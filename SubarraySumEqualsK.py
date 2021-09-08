class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Table = {"0":1}
        
        current_sum = 0
        count = 0
        for i in nums:
            current_sum += i
            
            if str(current_sum - k) in Table:
              ##if current_sum -k exists in Table already, guarantee a sum of a subarray = k####
              ###current_sum - k = value, current_sum - value = k, there exists a sum of a subarray = k and add the value(exsisted sum of a subarray start form index = 0) on it equals to current_sum###
                count += Table[str(current_sum - k)]
                
            if str(current_sum) in Table:
                Table[str(current_sum)] += 1
            else:
                Table[str(current_sum)] = 1
            
        return count
      ###O(n)
