# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    vals = {}
    for c in magazine:
        vals[c] = vals.get(c, 0) + 1
        
    for i in ransomNote:
        if vals.get(i, 0) <= 0: # avoid a keyerror if the key is not present
            return False
        vals[i] -= 1 # ensures each character is used only once
    return True