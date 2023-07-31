def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """            
        if len(nums) == 2 and k > 0:
            nums[0],nums[1] = nums[1], nums[0]
        else:
            nums[:] = nums[-k:] + nums[:-k]
        return nums