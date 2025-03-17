class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for num in nums:
            sum1 = sum1 + num
            while(num):
                digit = num%10
                sum2 = sum2 + digit
                num = num//10
        return sum1 - sum2

        