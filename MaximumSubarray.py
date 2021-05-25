class Solution:
    def maxSubArray(self,nums:List[int]) -> int:
        start = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            start = max(nums[i],nums[i] + start)
            res = max(start,res)
        return res
