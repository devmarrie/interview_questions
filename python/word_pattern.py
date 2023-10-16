# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

def wordPattern(pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        to_words = {}
        to_pat = {}

        for i in range(len(pattern)):
            char_p , word_s = pattern[i], words[i]
            if char_p in to_pat:
                if to_pat[char_p] != word_s:
                    return False
            else:
                to_pat[char_p] = word_s
            
            if word_s in to_words:
                if to_words[word_s] != char_p:
                    return False
                else:
                    to_words[word_s] = char_p
        return len(set(pattern)) == len(set(words))