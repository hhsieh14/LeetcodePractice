class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastIndex = len(digits) - 1
        carry = 0
        digits[lastIndex] += 1
        if digits[lastIndex] < 10:
            return digits
        output = []
        while lastIndex >= 0:#O(n)
            carry, digit = divmod(digits[lastIndex]+carry, 10)
            output.append(digit)
            lastIndex -= 1
        if carry > 0:
            output.append(carry)
        #cant use list.reverse()
        return output[::-1] #O(n)
