class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: #check constraints
            return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]#O(n)
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] #O(n)
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: #check constraints
                return 0
            else: 
                return int(revst)
            
    def reverse_v2(self, x):
        """
        :type x: int
        :rtype: int
        """
        store_digit = []
        negative = False
        if x < 0:
            negative = True
            x = x * -1
        rev = 0
        while x != 0:
            x, remain = divmod(x, 10)
            rev = rev*10 + remain
            
        if negative:
            rev *= -1
            
        if rev > (2**31 - 1) or rev < (2 ** 31)* -1:
            return 0
        
        return rev
