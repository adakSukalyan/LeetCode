class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)):
            if target ==nums[i]:
                return True
        else:
            return False