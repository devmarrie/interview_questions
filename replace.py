def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,k+1):
            nums[:] = nums[-1:] + nums[:-1]
        return nums