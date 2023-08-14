class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        total_tank = 0
        start = 0
    
        for i in range(n):
            tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
        
            if tank < 0:
                start = i + 1
                tank = 0
    
        if total_tank < 0:
            return -1
        else:
            return start