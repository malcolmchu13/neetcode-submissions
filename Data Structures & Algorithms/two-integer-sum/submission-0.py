class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash = {} 

        for i, n in enumerate(nums):
            Hash[n] = i 


        for i, n in enumerate(nums): 
            diff = target - n
            if diff in Hash and Hash[diff] != i: 
                return [i, Hash[diff]]
            


        
