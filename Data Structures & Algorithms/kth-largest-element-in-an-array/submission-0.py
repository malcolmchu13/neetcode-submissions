class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for i in nums: 
            heapq.heappush(maxheap, i)
            if len(maxheap) > k: 
                heapq.heappop(maxheap)
        
        return heapq.heappop(maxheap)

    