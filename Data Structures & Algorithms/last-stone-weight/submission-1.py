class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for x in stones: 
            heapq.heappush(heap, -x)
        if len(heap) == 1:
            return -(heapq.heappop(heap))
        while len(heap) > 1: 
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            new = (x-y)
            heapq.heappush(heap, new)
        return -(heapq.heappop(heap))
        
