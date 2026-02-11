class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        max_v=float('-inf')
        total=0
        for i in range(n):
            total=total+nums[i]
            max_v=max(max_v,total)
            if total<0:
                total=0
        return max_v