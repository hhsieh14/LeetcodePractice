class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            mem = target - nums[i]
            if str(nums[i]) in hashtable:
                return [hashtable[str(nums[i])], i]
            else:
                hashtable[str(mem)] = i
