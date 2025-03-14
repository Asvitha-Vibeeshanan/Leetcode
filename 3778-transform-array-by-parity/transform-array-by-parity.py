class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            if num%2 == 0:
                arr.append(0)
            else:
                arr.append(1)
        return sorted(arr)   