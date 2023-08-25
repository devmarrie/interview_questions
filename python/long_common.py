# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List
def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        lcp = ""
        strs.sort()
        first = strs[0]
        last = strs[n-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                break
            lcp += first[i]
        return lcp