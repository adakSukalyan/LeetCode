class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        long=0
        for i in num:
            if i-1 not in num:
                count=1
                x=i
                while x+1 in num:
                    count+=1
                    x+=1
                long=max(count,long)
        return long
