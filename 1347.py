class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        table = {}
        count = 0
        for c in s:
            if c not in table.keys():
                table[c] = 1
            else:
                table[c] += 1
                
        for c in t:
            if c in table.keys() and table[c] > 0:
                table[c] -= 1
            else:
                count += 1
                
        return count
"""
Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

"""
