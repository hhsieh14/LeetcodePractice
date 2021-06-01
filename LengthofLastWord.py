class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split() #O(n)
        if words:
            return len(words.pop()) #O(1)
        return 0
