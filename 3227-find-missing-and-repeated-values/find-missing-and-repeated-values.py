class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a,b=0,0
        expected_sum=0
        n=len(grid)
        actual_sum=((n*n)*((n*n)+1))//2
        nums=set()
        for i in range (n):
            for j in range(n):
                new_num=grid[i][j]
                expected_sum+=grid[i][j]
                if new_num in nums:
                    a=new_num
                nums.add(new_num)
        b=(actual_sum+a-expected_sum)
        rlist=[]
        rlist.append(a)
        rlist.append(b)
        return rlist