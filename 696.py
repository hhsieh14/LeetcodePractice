class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = s[0]
        num = []
        count = 0
        for i in s:
            if i == start:
                count += 1
            else:
                num.append(count)
                count = 1
                start = i
        num.append(count)
        result = 0
        for i in range(len(num)-1):
            result += min(num[i],num[i+1])
            
        return result
"""
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

#solution: convert into number list 
"""
