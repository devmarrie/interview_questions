def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        lcp = ""
        strs.sort()
        first = strs[0]
        last = strs[n-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                break
            lcp += first[i]
        return lcp