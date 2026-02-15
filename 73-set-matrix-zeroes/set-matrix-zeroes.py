class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        r=[-1 for _ in range(row)]
        c=[-1 for _ in range(col)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    r[i]=0
                    c[j]=0
        for i in range(row):
            for j in range(col):
                if r[i]== 0 or c[j]==0:
                    matrix[i][j]=0
    