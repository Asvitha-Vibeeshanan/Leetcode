class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # temp = original
        nums = sorted(nums, reverse = True)
        while(original in nums):
                original =  original * 2
            # else:
            #     original =     
        return original

        