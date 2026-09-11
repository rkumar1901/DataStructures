class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res, temp = [], []
        start = 1
            
        def tenta(start, temp):
            
            if len(temp) == k:
                res.append(temp.copy())
                return
            
            for i in range(start, n + 1):
                
                temp.append(i)
                tenta(i + 1, temp)
                temp.pop()
                
            
        tenta(start, temp)
        return res
        