# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_count = {}
        t_count = {}

        for char in s:
            s_count[char] = s_count.get(char, 0) + 1

        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        return s_count == t_count
