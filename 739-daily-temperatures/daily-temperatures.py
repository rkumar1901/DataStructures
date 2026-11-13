class Solution(object):
    def dailyTemperatures(self, temperatures):

        res = [0] * len(temperatures)

        temp = []

        for r in range(len(temperatures)):

            while temp and temperatures[r] > temperatures[temp[-1]]:
                x = temp.pop()
                res[x] = r - x

            temp.append(r)

        return res    
                

