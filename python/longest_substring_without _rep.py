# Given a string s, find the length of the longest
# substring
# without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(self, s: str) -> int:
        charUniq = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in charUniq:
                charUniq.remove(s[l])
                l += 1
            charUniq.add(s[r])
            res = max(r - l + 1, res)
        return res