class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            sign=-1
        else:
            sign=1
        n=abs(x)
        sum=0
        while(n!=0):
            rem=n%10
            n=n//10
            sum=(sum*10)+rem
        if sum< -2**31 or sum > 2**31-1:
            return 0
        return (sum*sign)