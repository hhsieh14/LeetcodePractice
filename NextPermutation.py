class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_peak = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                last_peak = i
                
        if last_peak == -1:
            l, r = (0, len(nums) - 1)
            while l < r:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                r -= 1
                l += 1
            return nums
        
        which_to_swap = 101
        for i in range(last_peak + 1, len(nums)):
            if nums[i] > nums[last_peak - 1] and nums[i] < nums[last_peak]:
                if nums[i] < which_to_swap:
                    which_to_swap = nums[i]
                    index = i
                    
        if which_to_swap == 101:
            temp = nums[last_peak]
            nums[last_peak] = nums[last_peak - 1]
            nums[last_peak - 1] = temp
        else:
            temp = nums[index]
            nums[index] = nums[last_peak - 1]
            nums[last_peak - 1] = temp
        nums[last_peak:] = sorted(nums[last_peak:])
        return nums
