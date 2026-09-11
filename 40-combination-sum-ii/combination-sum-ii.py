class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, temp = [], []
        start = 0
        cand = sorted(candidates)
        
        def tenta(start, temp):
            
            tot = sum(temp)
            
            if tot == target:
                res.append(temp.copy())
                return
            elif tot > target:
                return
            
            for i in range(start, len(cand)):

                if i > start and cand[i] == cand[i - 1]:
                    continue
                
                temp.append(cand[i])
                tenta(i+1, temp)
                temp.pop()
            
        
        tenta(start, temp)
        return res