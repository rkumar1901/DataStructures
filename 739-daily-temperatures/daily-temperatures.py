class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        res = [0] * len(temperatures)
        temp = []

        for r in range(len(temperatures)):

            while temp and temperatures[temp[-1]] < temperatures[r]:
                j = temp.pop()
                res[j] += r - j 

            temp.append(r)

        return res 



