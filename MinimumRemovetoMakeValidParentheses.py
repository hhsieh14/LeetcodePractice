class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        Stack = []
        
        for i, char in enumerate(s):
            if char == "(":
                Stack.append([char,i])
            if char == ")":
                if Stack and Stack[-1][0] == "(":
                    Stack.pop()
                else:
                    Stack.append([char,i])
                  
        start = 0
        for pairs in Stack:
            output += s[start:pairs[1]]
            start = pairs[1] + 1
            
        if start < len(s):
            output += s[start:]
        return output
      
###Time : O(n), Space: O(n)####
