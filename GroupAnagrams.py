class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        for s in strs:
            print(tuple(sorted(s)))
            new_s = ''.join(sorted(s))
            if new_s not in table:
                table[new_s] = [s, ]
            else:
                table[new_s].append(s)
        #output = []
        #for key in table:
        #    output.append(table[key])
        return table.values()
                
