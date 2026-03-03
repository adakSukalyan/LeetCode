class Solution:
    def findMin(self, nums: List[int]) -> int:
        min=float('inf')
        for i in range(len(nums)):
            if min>nums[i]:
                min=nums[i]
        return min