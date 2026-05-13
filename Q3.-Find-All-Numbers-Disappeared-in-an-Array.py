1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        numbers = set(nums)
4        res = []
5        for n in range(1, len(nums) + 1):
6            if n not in numbers:
7                res.append(n)
8        return res