1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        res=[]
4        for i in range(len(nums)):
5            count=0
6            for j in range(len(nums)):
7                if nums[i]>nums[j]:
8                    count+=1
9            res.append(count)
10        return res