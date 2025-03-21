class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        product1 = nums[0] * nums[1]
        product2 = nums[len(nums)-1] * nums[len(nums)-2]
        return abs(product1 - product2)