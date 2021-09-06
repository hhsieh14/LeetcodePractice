class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def outputtype(N,M):
            if N == M:
                return "{}".format(N)
            else:
                return "{}->{}".format(N,M)
        result = []
        if nums:
            #check with lower bound
            if nums[0] - lower != 0:
                result.append(outputtype(lower, nums[0] - 1))
            l = 0
            r = 1
            while r < len(nums):
                if nums[r] - nums[l] > 1:
                    result.append(outputtype(nums[l] + 1, nums[r] - 1))
                r += 1
                l += 1
            #check with upper bound
            if  upper - nums[-1] != 0:
                result.append(outputtype(nums[-1] + 1, upper))
            return result
        
        else:
            return [outputtype(lower, upper)]
