class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use set because remove operation is fast --> O(1)
        char_set = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            result = max(result, right - left + 1)
        return result
