class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        cand  = 0
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                cand += 2
            else:
                cand += 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                cand += 2
            else:
                cand += 1
        return cand
