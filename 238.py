class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ##devide the problem into prefix of the target and suffix of the target
        ##first construct an answer array storing prefix 
        answer = []
        answer.append(1)
        for i in range(1,len(nums)):
            answer.append(nums[i - 1] * answer[i - 1])
        ## use single var to multiply suffix to answer array
        j = len(answer) - 1
        back = 1
        while j >= 0:
            answer[j] *= back
            back *= nums[j]
            j -= 1
        return answer
      ##time: O(n) space: O(n)
