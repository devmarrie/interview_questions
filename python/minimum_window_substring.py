# Given two strings s and t of lengths m and n respectively, return the minimum window
# substring
# of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, countS = {}, {}
        for x in t:
            countT[x] = countT.get(x, 0) + 1
        m = float("inf")
        res = [-1, -1]
        l = 0
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            countS[c] = countS.get(c,0) + 1

            if c in countT and countS[c] == countT[c]:
                have += 1
                
            while have == need:
                if (r - l + 1) < m:
                    res = [l,r]
                    m = (r - l + 1)
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return "" if m == float("inf") else s[l:r+1]