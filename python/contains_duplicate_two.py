# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        vals = {}
        for k, v in enumerate(nums):
            if v in vals:
                vals[v].append(k)
            else:
                vals[v] = [k]
        for z in vals.values():
           if len(z) >= 2:
               i = 0
               for j in range(len(z)):
                    if abs(z[i] - z[j]) <= k:
                        return True
                    i += 1
        return False