class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_val=float('-inf')
        n=len(arr)
        for i in range(n):
            if max_val<arr[i]:
                max_val=arr[i]
                index=i
        return index