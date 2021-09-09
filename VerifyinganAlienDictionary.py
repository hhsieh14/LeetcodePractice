class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        ordermap = {}
        for index, val in enumerate(order): #O(26)
            ordermap[val] = index
            
        i = 0
        while i < len(words) - 1:#O(N)
            point1 = 0
            point2 = 0
            while point1 < len(words[i]) and point2 < len(words[i + 1]):#O(M)
                if ordermap[words[i][point1]] > ordermap[words[i + 1][point2]]:
                    return False
                elif ordermap[words[i][point1]] < ordermap[words[i + 1][point2]]:
                    break
                point1 += 1
                point2 += 1
            if point1 < len(words[i]) and point2 >= len(words[i+1]): 
                return False
            i += 1
        return True
##Time: O(NM)
