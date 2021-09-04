class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0 
        right = 0
        maxlen = 0
        charlist = {}
        while right < len(s):
            
            charlist[s[right]] = right
            
            if len(charlist) < 3:
                maxlen = max(maxlen, right - left + 1)
                right += 1
                
            else:
                min_value = min(charlist.values())
                left = min_value + 1
                del charlist[s[min_value]]
                
        return maxlen
