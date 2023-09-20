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
        res = 0
        i = 0
        if s == "":
            return 0
        if not s.strip():
            return 1
        if len(s) == 1:
            return 1
        sub = f"{s[0]}"        
        for j in range(1, len(s)):
            if s[j] != s[i] and s[j] not in sub:
                sub += s[j]
                if len(s) == 2 and s == sub:
                    return 2
                i += 1
            else:
                res = max(len(sub), res)
                sub = f"{s[j]}"
                i = j
                j = i + 1
        print(res)
        return res