class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        temp = x
        while(x):
            digit = x%10
            x = x//10
            sum = sum + digit
        if temp%sum == 0:
            return sum
        else:
            return -1 