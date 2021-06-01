class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        j = 0
        for i in range(m,m+n):#O(n)
            nums1[i] = nums2[j]
            j += 1
        nums1.sort() #O((m+n)log(m+n)), Timsort
