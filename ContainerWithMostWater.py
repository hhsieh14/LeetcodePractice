class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        i,j = 0,len(height)-1
        while i < j:
            vol = (j - i)*min(height[i], height[j])
            if vol > max_vol:
                max_vol = vol
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_vol
