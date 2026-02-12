class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[0]*l
        p=0
        n=1
        for i in range(l):
            if (nums[i]>0):
                res[p]=nums[i]
                p+=2
            else:
                res[n]=nums[i]
                n+=2
        return res
