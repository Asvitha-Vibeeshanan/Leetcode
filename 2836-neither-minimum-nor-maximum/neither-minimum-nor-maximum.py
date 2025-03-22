class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) == 2 or len(nums) == 1:
            return -1
        for num in nums:
            if num != min(nums) and num != max(nums):
                return num