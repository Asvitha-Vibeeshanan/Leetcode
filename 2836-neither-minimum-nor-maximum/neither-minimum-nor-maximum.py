class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        if len(nums) == 2 or len(nums) == 1:
            return -1
        else:
            nums = sorted(nums)
            return nums[1]