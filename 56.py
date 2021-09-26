class Solution(object):
    def merge(self, intervals, current = 0):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        current = 0
        for start, end in sorted(intervals, key = lambda x:x[0]):
            print(output)
            if not output:
                output.append([start,end])
            else:
                if output[current][1] >= start:
                    output[current] = [output[current][0],max(end,output[current][1])]
                else:
                    current += 1
                    output.append([start,end])
        return output
      ##O(nlog(n))
