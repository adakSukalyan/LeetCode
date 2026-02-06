class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        num=0
        numl=[]
        for i in range(len(nums)):
            new_num=nums[i]
            new_count=0
            if new_num in numl:
                continue
            numl.append(new_num)
            for j in range(len(nums)):
                if new_num == nums[j]:
                    new_count+=1
            if count<new_count:
                num=new_num
                count=new_count
        return num