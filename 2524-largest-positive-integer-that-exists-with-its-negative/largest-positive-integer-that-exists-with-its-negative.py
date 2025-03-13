class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        arr = []
        arr1 = [abs(nums[i]) for i in range(len(nums)) if nums[i]<0]
        arr2 = [nums[i] for i in range(len(nums)) if nums[i]>0]
        return max(list(set(arr1)&set(arr2))) if list(set(arr1)&set(arr2)) else -1