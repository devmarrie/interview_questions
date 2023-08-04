def jump(self, nums: List[int]) -> int:
        jumps = 0
        n = len(nums)
        current_max_reach = nums[0]
        next_max_reach = nums[0]

        for i in range(1, n):
            if i > current_max_reach:
               jumps += 1
               current_max_reach = next_max_reach

            next_max_reach = max(next_max_reach, i + nums[i])
        if len(nums) > 1:
            return jumps + 1
        else:
            return 0