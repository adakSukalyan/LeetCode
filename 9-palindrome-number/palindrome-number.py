class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=abs(x)
        sum=0
        while(n!=0):
            rem=n%10
            n=n//10
            sum=(sum*10)+rem

        rev=sum
        if(rev==x):
            return True
        else:
            return False