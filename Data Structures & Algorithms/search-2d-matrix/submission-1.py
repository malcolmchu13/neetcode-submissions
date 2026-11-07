class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        top, bot = 0, len(matrix) - 1

        while top <= bot: 
            mid = (top+bot) //2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target: 
                break 
            elif matrix[mid][0] > target : 
                bot = mid -1
            elif matrix[mid][-1] < target: 
                top = mid + 1

        row = matrix[mid]
        l, r = 0, len(row) - 1
        while l <= r: 
            middle = (l+r)//2
            if row[middle] == target: 
                return True 
            elif row[middle] < target: 
                l = middle + 1  
            elif row[middle] > target: 
                r = middle - 1 

        return False


        




