def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words)
        new = ""
        for i in range(n-1, -1, -1):
            new += words[i]
            if i != 0:
                new += " "
        return new