class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=[]
        minn=float('inf')
        for i in range(len(strs)):
            if len(strs[i]) < minn:
                minn=len(strs[i])
        for i in range(minn):
            for j in range(len(strs)):
                key=strs[0][i]
                if strs[j][i] !=key:
                    return "".join(res)
            res.append(key)
        return "".join(res)