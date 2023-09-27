def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = ""
        emp = []
        l = 0
        w_cut = len(words[0])
        wlen = len(words) * w_cut
        tog = []
        w_perm = set(''.join(p) for p in permutations(words))

        # Hash map for how many times the word occours
        wcnt, seen = {}, {}
        for c in words:
            wcnt[c] = wcnt.get(c, 0) + 1

        for r in range(len(s)):
            res += s[r]
            if len(res) == wlen:
                emp.append(res)
                print(res[:w_cut])
                for perm in w_perm:
                    if perm in res:
                       tog.append(l)
                res = res[1:]
                l += 1
        print(emp)
        

        # for i in range(len(emp)):
        #     if any(perm in emp[i] for perm in w_perm):
        #         tog.append(i)
        return tog