1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3        k=set()
4        res=[]
5        for i in range(len(nums)):
6            if nums[i] not in k:
7                k.add(nums[i])
8            else:
9                res.append(nums[i])
10        for i in range(1,len(nums)+1):
11            if i not in nums:
12                res.append(i)
13        return res
14
15