class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
        ###2一定比5早出現,算5幾個就好##O(logn)以5為底
