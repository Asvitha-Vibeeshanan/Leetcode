class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if nums == [0]:
            return nums
        arr1,arr2 = [], []
        for num in nums:
            if num% 2 == 0:
                arr2.append(num)
            else:
                arr1.append(num)
        return (arr2 + arr1)