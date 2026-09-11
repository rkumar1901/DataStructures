class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res, temp = [], []
        n = len(nums)
        start = 0
        
        def tenta(start, temp):
            res.append(temp.copy())
            
            for i in range(start, n):
                
                temp.append(nums[i])
                tenta(i + 1, temp)
                temp.pop()
            
        
        tenta(start, temp)
        return res
        