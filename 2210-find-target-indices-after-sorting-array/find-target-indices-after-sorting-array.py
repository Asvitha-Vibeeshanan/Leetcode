class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        arr = []
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        return arr


        