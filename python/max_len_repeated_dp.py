# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

# Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].

# Example 2:

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
from typing import List
def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        mlen = 0

        for y in range(len(nums1) -1, -1, -1):
            for x in range(len(nums2) -1, -1, -1):
                if nums1[y] == nums2[x]:
                    dp[y][x] = dp[y + 1][x + 1] + 1
                    mlen = max(dp[y][x], mlen)
        return mlen 

