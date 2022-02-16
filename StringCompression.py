class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.reverse() ##O(n)
        output = 0
        count = 1
        n_iterations = len(chars) - 1
        
        for i in range(n_iterations):
            if chars[i] != chars[i+1]:
                
                if count > 1:
                    for n in str(count)[::-1]:
                        chars.append(n)
                        output += 1
                chars.append(chars[i])
                count = 1
                output += 1
                
            if chars[i] == chars[i+1]:
                count += 1
        
        
        if count  > 1:
            for n in str(count)[::-1]:
                        chars.append(n)
                        output += 1
            
        chars.append(chars[n_iterations])
        output += 1
        
        chars.reverse()
        return output
