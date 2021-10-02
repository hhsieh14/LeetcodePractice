class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        index = len(heights) - 2
        max_val = heights[-1]
        result = [index + 1,]
        while index >= 0:
           
            if heights[index] > max_val:
                result.append(index)
                max_val = heights[index]
           
                
            index -= 1
        return reversed(result)
