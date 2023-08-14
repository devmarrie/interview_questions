class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            total_gas = 0
            for stn in range(n):
                curr = (i+stn) % n
                total_gas += gas[curr] - cost[curr]
                if total_gas < 0:
                    break
            if total_gas >= 0:
                return i
        return -1