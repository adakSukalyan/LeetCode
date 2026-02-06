class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numl=set()
        for i in range(len(nums)):
            num=nums[i]
            if num in numl:
                return True
            numl.add(num)
        else:
            return False