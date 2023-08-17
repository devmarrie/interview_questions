class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            t = 0
        else:
            t = height[0]
        for i in range(1, n):
            if height[i-1] > height[i]:
                t +=  height[i-1] - height[i]
        return t