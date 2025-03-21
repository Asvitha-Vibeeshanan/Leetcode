class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = 0
        r = len(nums)-1
        max = 0
        while(l<r):
            if (nums[l] + nums[r]) > max:
                max = nums[l] + nums[r]
            l = l+1
            r = r-1
        return max 