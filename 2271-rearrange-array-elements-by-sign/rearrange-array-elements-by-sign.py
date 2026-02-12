class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        list1=[]
        list2=[]
        list3=[]
        for i in range(n):
            if (nums[i]>0):
                list1.append(nums[i])
            else:
                list2.append(nums[i])
        for j in range(n//2):
                list3.append(list1[j])
                list3.append(list2[j])
        return list3