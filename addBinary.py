class Solution:
  def addBinary(self, a: str, b: str) -> str:
    return(bin(int(a,2) + int(b,2))[2:])
  #https://www.coder.work/article/6860745
  #the link shows timecomplexity of bin() is O(log(n))
  #https://stackoverflow.com/questions/44025315/what-is-the-time-complexity-of-int1010-2
  #the link shows the int(,2) binary based covertion is O(n)
  #return substring is also O(n)
  #total = O(n + n + log(n) + n) --> O(3n + log(n))
#below is my solution --> O(n)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #check which one is longer
        if len(a) >= len(b):
            shortIndex = len(b) - 1
            longIndex = len(a) - 1
            long = a
            short = b
        else:
            shortIndex = len(a) - 1
            longIndex = len(b) - 1
            long = b
            short = a
        carry = 0
        output = ""
        #according to the length add from short to long
        #O(n), n = longest string
        while shortIndex >= 0:
            carry, digit = divmod(int(short[shortIndex])+int(long[longIndex])+carry, 2)
            output += str(digit)
            shortIndex -= 1
            longIndex -= 1
        while longIndex >= 0:
            carry, digit = divmod(int(long[longIndex])+carry, 2)
            output += str(digit)
            longIndex -= 1
        #check if last one is 1 or not
        if carry > 0:
            output += str(carry)
        #cant use list.reverse()
        return output[::-1] #O(n)
