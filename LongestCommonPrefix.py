class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        sortedlist = sorted(strs, key=len) #O(nlogn)
        prefix = sortedlist[0] 
        if prefix == "":
            return ""
        for word in sortedlist[1:]:
            for j in range(len(prefix)):
                if prefix[j] != word[j]:
                    prefix = prefix[:j]
                    break
                    
        return prefix
