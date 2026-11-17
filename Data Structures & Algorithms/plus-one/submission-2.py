class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastindex = len(digits) -1 
        while lastindex >= 0:
            if digits[lastindex] == 9: 
                digits[lastindex] = 0 
                lastindex -= 1 
            else: 
                digits[lastindex] = digits[lastindex] + 1 
                break
        if lastindex == -1: 
            digits[lastindex] = 0
            digits.insert(0,1)    

        return digits
            