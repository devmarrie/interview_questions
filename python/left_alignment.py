def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tt_width = 0
        line = []
        out = []
        for word in words:
            if tt_width + len(line) + len(word) <= maxWidth:
                line.append(word)
                tt_width += len(word)
            else:
                spaces = maxWidth - tt_width
                if len(line) == 1:
                    out.append(line[0] + " " * spaces)
                else:
                    gaps = len(line) - 1
                    extra = spaces // gaps
                    rem = spaces % gaps

                    for i in range(len(line) -1):
                        line[i] += " " * extra
                        if rem > 0:
                            line[i] += " "
                            rem -= 1
                    out.append("".join(line))
                line = [word]
                tt_width = len(word)
        #left justify the curr line
        last_line = ' '.join(line).ljust(maxWidth)
        out.append(last_line)
        return out
