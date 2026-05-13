class Solution:
    [-1,0,2,4,6,8]
    def search(self, nums: List[int], target: int) -> int:
        low,high =0,len(nums)-1

        if nums[low]==target:
            return low

        if nums[high]==target:
            return high

        while low < high-1:
            mid=(low+high) // 2

            if nums[mid]==target:
                return mid 

            if nums[mid]>target :
                high=mid
            else:
                low=mid
            

        return -1