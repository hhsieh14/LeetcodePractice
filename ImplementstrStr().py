class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle:
            return 0
        
        n = len(needle) - 1
        index = 0
        for i in range(len(haystack) - n):
            if haystack[i:i+n+1] == needle:
                return i
        return -1
