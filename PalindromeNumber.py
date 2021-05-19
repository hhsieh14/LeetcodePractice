class Solution:
    def isPalindrome(self, x: int) -> bool:
        strg = str(x)
        i = 0
        j = len(strg) - 1
        while i < j:
            if strg[i] != strg[j]:
                return False
            i += 1
            j -= 1
        return True
