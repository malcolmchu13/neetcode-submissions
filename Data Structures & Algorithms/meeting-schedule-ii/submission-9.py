"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []

        if not intervals: 
            return 0 

        for i in intervals:
            heapq.heappush(heap, i.end)
            if i.start >= heap[0]: 
                heapq.heappop(heap)
            
        return len(heap)


            


        

