class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c=-1
        f=-1
        l=-1
        for i in range(len(nums)):
            if target==nums[i]:
                f=i
                c=i
                break
        count=0
        if f==-1:
            return [-1,-1]
        while(c+1 < len(nums) and nums[c]==nums[c+1] ):
            l=c+1
            c+=1
            count+=1
        if count ==0 :
            l=f
        return [f,l]