class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for i in range(len(digits)):
            sum = (sum * 10) + digits[i]

        new = sum + 1
        digits.clear()
        while new != 0:
            rem = new % 10
            new=new//10
            digits.append(rem)
        digits.reverse()
        return digits