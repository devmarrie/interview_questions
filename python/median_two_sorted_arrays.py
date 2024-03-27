# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            a = nums2
            b = nums1
        else:
            a = nums1
            b = nums2
        
        l, r = 0, len(a)-1
        while True:
            i =  (l + r) // 2 # median for the shortest list
            j = half - i - 2 # we are finding the index and list starts from 0

            aleft = a[i] if i >= 0 else float("-infinity")
            aright = a[i+1] if (i+1) < len(a) else float("+infinity")
            bleft = b[j] if j >= 0 else float("-infinity")
            bright = b[j+1] if (j+1) < len(b) else float("+infinity")

            if aleft <= bright and bleft <= aright:
                #odd
                if total % 2:
                    return min (aright, bright)
                else:
                    return (min(aright, bright) + max(aleft, bleft)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1