class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        for i in range(n):
            total_gas += gas[i] - cost[i]
            for stn in range(n):
                curr = (i+stn) % n
                total_gas += gas[curr]
                if total_gas < 0:
                    return i
                else:
                    return -1