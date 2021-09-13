class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        output = ""
        while i >= 0 and j >= 0:
            carry, digit = divmod(int(num1[i]) + int(num2[j]) + carry, 10)
            output = str(digit) + output
            i -= 1
            j -= 1
            
        while i >= 0:
            carry, digit = divmod(int(num1[i]) + carry, 10)
            output = str(digit) + output
            i -= 1
           
        while j >= 0:
            carry, digit = divmod(int(num2[j]) + carry, 10)
            output = str(digit) + output
            j -= 1
            
        if carry > 0:
            output = str(carry) + output
        return output
##O(max(N,M)
