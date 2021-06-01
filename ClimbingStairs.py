class Solution:
    def climbStairs(self, n: int) -> int:
        table = [1, 2]
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(2, n):
            table.append(table[i-1]+table[i-2])
            
        return table[-1]
   
  
#[1,2,3,5,8,....]
#Fibonacci Number
