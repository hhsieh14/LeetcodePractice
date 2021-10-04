class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        
        table = {}
        for strs in strings:
            key = ''
            for i in range(len(strs) - 1):
                temp = ord(strs[i+1]) - ord(strs[i])
                if temp < 0: 
                    temp += 26
                key += str(temp)+'.'
                
            if key not in table:
                table[key] = [strs, ]
            else:
                table[key].append(strs)
        #print(table)
        return table.values()
