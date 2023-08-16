class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        cand  = 0
        for i in range(n):
            if i == 0 and ratings[i] > ratings[i+1]:
               cand += 2
            elif i == n - 1 and ratings[i] > ratings[i-1]:
                cand += 2
            elif 0 < i < n-1 and (ratings[i] > ratings[i+1] or ratings[i] >   ratings[i-1]):
                cand += 2
            else:
                cand += 1
        return cand
