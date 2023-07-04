class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) and sorted(s) != sorted(goal):
            return False
        if len(s) == 2 and len(goal) == 2:
            if s[0] == goal[1] and s[1] == goal[0]:
                return True
        if len(s) > 2 and len(goal) > 2:
           if s == goal:
              return True
        count = 0
        arr_diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                arr_diff.append(i)
        if count > 2:
            return False
        if len(arr_diff) != 2:
            return False
        char_1 = arr_diff[0]
        char_2 = arr_diff[1]
        return s[char_1] == goal[char_2] and s[char_2] == goal[char_1]
