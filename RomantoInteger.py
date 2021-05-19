class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        numbers = []
        for Roman in s:
            numbers.append(table[Roman])
        for i in range(len(numbers)-1):
		        if numbers[i]<numbers[i+1]:
			        numbers[i] = -numbers[i]     
        return sum(numbers)
