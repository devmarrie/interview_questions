# def isSubsequence(self, s: str, t: str) -> bool:
#         sub = ""
#         fst = 0
#         n = len(s)
#         for char in t:
#             if fst < n and char == s[fst]:
#                 sub += char
#                 fst += 1
#         print(sub)
#         return sub == s
def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)