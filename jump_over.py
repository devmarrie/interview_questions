class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 2 and nums[0] == 0:
            return False

        first_index = 1
        while first_index < len(nums):
            val = nums[first_index]
            if val == 0:
                return False
            first_index += val
        return True
