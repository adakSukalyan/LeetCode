class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expected=(n*(n+1))//2
        actual=0
        for i in range(len(nums)):
            actual+=nums[i]
        return expected-actual