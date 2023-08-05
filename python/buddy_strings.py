"""
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

 

Constraints:

    1 <= s.length, goal.length <= 2 * 104
    s and goal consist of lowercase letters.


"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # contain simmilar characters
        for char in s:
            if char not in goal:
                return False
                
        """ Only two characters"""
        if len(s) == 2 and len(goal) == 2:
            if s[0] == goal[1] and s[1] == goal[0]:
                return True
        # both strings are identical
        if len(s) > 2 and len(goal) > 2:
           if s == goal:    
              for q in range(len(s)):
                  for r in range(q+1, len(s)-1):
                      if s[q] == goal[r] and s[r] == goal[q]:
                          return True

        count = 0
        arr_diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                arr_diff.append(i)
                if count > 2:
                    return False
                if s.count(s[i]) > 1 and s[i] == goal[i]:
                    return False
                
            for j in range(i+1, len(s)-1):
                # if j in char_count:
                #     char_count[j] += 1
                #     if char_count[j] > len(s) // 2:
                #         return False
                if s[i:j+1] == s[j+1:j+1+(j-i+1)] and s[j] == goal[j]:
                    return True
                
        if count != 2:
            return False
        if len(arr_diff) != 2:
            return False
        char_1 = arr_diff[0]
        char_2 = arr_diff[1]
        return s[char_1] == goal[char_2] and s[char_2] == goal[char_1]
