class Solution:
    def isValid(self, s: str) -> bool:
        #, ')':'(', '}':'{' , ']':'['
        table = {'(' : ')', '{' : '}', '[':']'}
        stack = []
        if s[0]in table:
            stack.append(table[s[0]]) 
        else:
            return False
        for p in s[1:]:
            #check if the stack is not empty and match
            if stack and p == stack[-1]:
                stack.pop()
            #check we only append left parentheses
            elif p in table:
                stack.append(table[p])
            else:
                return False
                
        if len(stack) == 0:
            return True
        else:
            return False
