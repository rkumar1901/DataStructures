class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        if sum(gas) < sum(cost):
            return -1

        start, current_gas = 0, 0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            
            # If the current gas goes negative, reset the starting station
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        
        return start
        
        