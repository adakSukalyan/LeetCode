class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        res=[]
        srow=0
        erow=n-1
        scol=0
        ecol=m-1
        while(srow<=erow and scol<=ecol):
            for i in range(scol,ecol+1):
                res.append(matrix[srow][i])

            for i in range(srow+1,erow+1):
                res.append(matrix[i][ecol])

            for i in range(ecol-1,scol-1,-1):
                if (srow==erow):
                    break
                res.append(matrix[erow][i])

            for i in range(erow-1,srow,-1):
                if (scol==ecol):
                    break
                res.append(matrix[i][scol])
            srow+=1
            erow-=1
            scol+=1
            ecol-=1
        return res

        