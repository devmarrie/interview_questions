def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        lcp = ""
        if len(strs) == 1:
            lcp += strs[0] 
        for i in range(n):
            if i+1 < n and i+2 < n:
                for char in strs[i]:
                    if char in strs[i+1] and char in strs[i+2]:
                        lcp += char
        return lcp