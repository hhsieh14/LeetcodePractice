class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        count = 0
        while l < r:
            if s[l] != s[r]:
                count += 1
                state1 = self.check(s[l:r])
                state2 = self.check(s[l + 1:r + 1])
                if state1 == False and state2 == False:
                    return False
                if state1 == True or state2 == True:
                    if count <= 1 and len(s) > 3:
                        return True
            l += 1
            r -= 1
        if count > 1:
            return False
        else:
            return True
    ###O(N) for two pointers check along the list####
    def check(self, substr):
        l = 0
        r = len(substr) - 1
        count = 0
        while l < r:
            if substr[l] != substr[r]:
                return False
            l += 1
            r -= 1
        return True
