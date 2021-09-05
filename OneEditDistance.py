class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s)
        tlen = len(t)
        if abs(len(s) -len(t)) > 1 or s == t:
            return False
        i = 0
        j = 0
        count = 0
        while i < slen and j < tlen:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                count += 1
                if slen > tlen:
                    i += 1
                elif slen < tlen:
                    j += 1
                else:
                    i += 1
                    j += 1
                
        if count < 2:
            return True
        else:
            return False
#####Time: O(max(N,M)); Space: O(1)######
