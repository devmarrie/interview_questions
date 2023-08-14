class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        for i in range(n):
            indx = i % n
            tank += gas[indx]
            count = gas[indx] - cost[indx]
            curr_tank = count + gas[indx+1]
            if count < 0:
                indx += 1
                tank = 0
                break
            
        if curr_tank > gas[i+1]:
                return i
        return -1