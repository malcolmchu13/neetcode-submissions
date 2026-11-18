class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r: 
            mid = (l + r) //2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
            if totalTime <= h: 
                r = mid 
            elif totalTime >=h : 
                l = mid + 1
        return l