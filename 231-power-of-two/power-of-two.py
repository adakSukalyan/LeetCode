class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        it=int(n**0.5)+2
        for i in range(it):
            if 2**i ==n:
                return True
        else:
            return False