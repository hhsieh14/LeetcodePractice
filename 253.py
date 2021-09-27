class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x: x[0])
        rooms = []
        min_val = float('inf')
        
        for start, end in intervals:
            if not rooms:
                rooms.append(end)
                min_val = end
            else:
                if min_val <= start:
                    rooms[rooms.index(min_val)] = end
                else:
                    rooms.append(end)
                min_val = min(rooms)
            
                    
        
        return len(rooms)
