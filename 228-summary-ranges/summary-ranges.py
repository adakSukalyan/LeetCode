class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n=len(nums)
        res=[]
        i=0
        while(i<n):
            st=nums[i]
            end=nums[i]
            while( i+1<n and nums[i]==nums[i+1]-1):
                i+=1
                end=nums[i]
            if st==end:
                res.append(str(st))
            else:
                res.append(str(st)+"->"+str(end))
            i+=1
        return res