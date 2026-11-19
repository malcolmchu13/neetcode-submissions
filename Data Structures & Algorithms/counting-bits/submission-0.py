class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for n in range(n + 1):
            count = 0
            num = n 
            while num > 0:
                count += num % 2   
                num //= 2       
            res.append(count) 
        return res



        