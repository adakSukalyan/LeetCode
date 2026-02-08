class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for j in range(len(nums)):
            if (nums[j] != 0):
                nums[k], nums[j] = nums[j], nums[k]
                k += 1