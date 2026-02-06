class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        numl=[]
        for i in range(len(nums)):
            new_num=nums[i]
            if new_num in numl:
                return new_num
            numl.append(new_num)
           