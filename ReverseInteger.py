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
