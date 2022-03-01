class Solution:
    def convert(self, s: str, numRows: int) -> str:
        storage = [""]*numRows
        track_id = 0
        positive_direction = True
        for character in s:
            storage[track_id] += character
            if positive_direction:
                track_id += 1
            else:
                track_id -= 1
                
            if track_id >= numRows:
                positive_direction = False
                track_id -= 2
            elif track_id < 0:
                positive_direction = True
                track_id += 2
        return ''.join(storage)
