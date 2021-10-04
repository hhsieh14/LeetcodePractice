class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in s:
            if stack and stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
