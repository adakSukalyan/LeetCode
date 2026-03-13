class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        for i in range (rowIndex+1):
            row=[1]*(1+i)
            for j in range(1,len(row)-1):
                row[j]=res[i-1][j-1] +res[i-1][j]
            res.append(row)
        return res[rowIndex]

