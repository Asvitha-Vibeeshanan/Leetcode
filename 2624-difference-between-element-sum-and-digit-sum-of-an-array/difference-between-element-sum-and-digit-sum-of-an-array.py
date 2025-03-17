class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for num in nums:
            sum1 = sum1 + num
            while(num):
                sum2 = sum2 + num%10
                num = num//10
        return sum1 - sum2