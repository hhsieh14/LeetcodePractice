class Solution:
    def mySqrt(self, x: int) -> int:
        lower = 0
        upper = x
        while int(lower) < int(upper):
            mid = (lower + upper)/2
            if mid ** 2 > x:
                upper = mid
            else:
                lower = mid
        return int(lower)
