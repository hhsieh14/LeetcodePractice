class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        table = {}
        for i, num in enumerate(nums):
            if num != 0:
                table[i] = num
        self.table = table
        self.nums = nums
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        result = 0
        for key in self.table:
            result += self.table[key] * vec.nums[key]
        return result
    
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
