class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        state = {}
        correct = {} 

        if len(s2) < len(s1):
            return False
        
        for i in range(len(s1)): 
            correct[s1[i]] = correct.get(s1[i],0) + 1 


        for i in range(len(s2)): 
            state[s2[i]] = state.get(s2[i],0) + 1
            if i - l + 1 == len(s1):
                if state == correct: 
                    return True 
                else: 
                    state[s2[l]] -= 1
                    if state[s2[l]] == 0:
                        del state[s2[l]]
                    l+=1
        return False
            
            

