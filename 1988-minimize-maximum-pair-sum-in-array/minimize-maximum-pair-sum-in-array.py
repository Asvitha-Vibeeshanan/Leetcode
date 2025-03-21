class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = 0
        r = len(nums)-1
        max = 0
        while(l<r):
            sum = nums[l] + nums[r]
            if sum > max:
                max = sum
            l = l+1
            r = r-1
        return max 