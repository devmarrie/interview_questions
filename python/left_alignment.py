def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tt_width = 0
        line = []
        out = []
        for word in words:
            if tt_width + len(line) + len(word) <= maxWidth:
                line.append(word)
                tt_width += len(word)
            spaces = maxWidth - tt_width
            each = spaces // max(1,len(line) - 1)
            extra = spaces % max(1,len(line) - 1)
            for i in range(max(1,len(line) - 1)):
                line[i] += " " * each
                if extra:
                   line[i] += " "
                   extra -= 1
            out.append("".join(line))
            line, tt_width = [], 0
        return out