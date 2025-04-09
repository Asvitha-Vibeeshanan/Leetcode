class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)+1):
            if i != 0 and len(nums)%i == 0:
                sum = sum + (nums[i-1] * nums[i-1])
        return sum