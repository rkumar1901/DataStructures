class Solution(object):
    def dailyTemperatures(self, temperatures):

        res = [0] * len(temperatures)
        temp = []

        for i in range(len(temperatures)):

            while temp and temperatures[temp[-1]] < temperatures[i]:
                j = temp.pop()
                res[j] += i - j 
            
            
            temp.append(i)

        return res