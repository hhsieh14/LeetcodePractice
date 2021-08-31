class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
       
        def getlength(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1 #記得減一
        start = 0
        length = 0
        for i in range(n):
            substring_len = max(getlength(i,i), getlength(i,i+1))
            if substring_len <= length: continue #find maximun substring
            length = substring_len
            start = i - (substring_len - 1)// 2
        return s[start: start + length]
