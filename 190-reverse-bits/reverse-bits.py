class Solution:
    def reverseBits(self, n: int) -> int:
        res=""
        while n>0:
            rem=n%2
            res+=str(rem)
            n=n//2
        x=res
        if len(x) !=32 and len(x) < 32:
            zero=32-len(x)
            for i in range(zero):
                x+="0"
        deci=0
        power=len(x)-1
        for i in range(len(x)):
            deci+=int(x[i])*(2**power)
            power-=1
        return deci