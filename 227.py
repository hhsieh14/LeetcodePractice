class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        
        new_s = ''
        operations = []
        numbers = [str(x) for x in range(10)]
        for i in s:
            if i != ' ':
                new_s += str(i)
                if i not in numbers:
                    operations.append(str(i))
                    
        stack = []
        new_s = list(map(int, re.split('[-+*/]', new_s)))
       
        stack.append(new_s[0])
        for i in range(1, len(new_s)):
          
            if operations[i-1] == '-':
                new_s[i] = -1 * new_s[i]
                stack.append(new_s[i])
            elif operations[i - 1] == '*':
                stack.append(stack.pop() * new_s[i])
            elif operations[i - 1] == '/':
                if stack[-1] < 0:
                    new_val = -1 * int(-1*stack.pop() / new_s[i])
                else:
                    new_val = stack.pop() / new_s[i]
                stack.append(new_val)
            else:
                stack.append(new_s[i])
        
        return sum(stack) 
