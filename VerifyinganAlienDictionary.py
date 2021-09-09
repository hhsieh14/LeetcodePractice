class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        i = 0
        while i < len(words) - 1:
            point1 = 0
            point2 = 0
            while point1 < len(words[i]) and point2 < len(words[i + 1]):
                if order.index(words[i][point1]) > order.index(words[i + 1][point2]):
                    return False
                elif order.index(words[i][point1]) < order.index(words[i + 1][point2]):
                    break
                point1 += 1
                point2 += 1
            if point1 < len(words[i]) and point2 >= len(words[i+1]): 
                return False
            i += 1
        return True
##Time: O(NM)
