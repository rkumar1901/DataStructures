class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res, temp = [], []
        start = 0
        cand = candidates
        
        def tenta(start, temp):
            
            tot = sum(temp)
            
            if tot == target:
                res.append(temp.copy())
                return
            elif tot > target:
                return
            
            for i in range(start, len(cand)):
                
                temp.append(cand[i])
                tenta(i, temp)
                temp.pop()
            
        
        tenta(start, temp)
        return res
        