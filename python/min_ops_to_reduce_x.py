# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1

# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
from typing import List
def minOperations(nums: List[int], x: int) -> int:
        target = sum(nums) - x
        curr_sum = 0
        max_window = -1
        l = 0

        for r in range(len(nums)):
            curr_sum += nums[r]

            while l < r and curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            
            if curr_sum == target:
                max_window = max(max_window, r - l + 1)
        
        return -1 if max_window == -1 else len(nums) - max_window