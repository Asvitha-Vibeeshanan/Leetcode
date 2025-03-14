class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        val = ""
        l = 0
        r = len(nums) - 1
        res = 0
        if len(nums) % 2 == 0:
            while(l < r):
                val = str(nums[l]) + str(nums[r])
                res = res + int(val)
                val = ''
                l = l + 1
                r = r - 1
            return res
        else:
            mid = len(nums)//2
            while(l < r):
                val = str(nums[l]) + str(nums[r])
                res = res + int(val)
                val = ''
                l = l + 1
                r = r - 1
            return res + nums[mid]