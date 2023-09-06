def isSubsequence(self, s: str, t: str) -> bool:
        sub = ""
        fst = 0
        n = len(s)
        for char in t:
            if fst < n and char == s[fst]:
                sub += char
                fst += 1
        print(sub)
        return sub == s