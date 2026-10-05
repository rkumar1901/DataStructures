class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        if sum(gas) < sum(cost):
            return -1

        start = 0
        current_gas = 0
        for i in range(len(gas)):

            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start = i + 1
                current_gas = 0

        return start 
            
        
        