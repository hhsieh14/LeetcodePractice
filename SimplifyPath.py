class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        new_path = path.split('/') #O(n)
        result = []
        for filename in new_path:
            if filename == '.' or not filename:
                continue
            elif filename == '..':
                if result:
                    result.pop()
            else:
                result.append(filename)
        return '/' + '/'.join(result)
