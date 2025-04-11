class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        sum = 0
        for key, value in dict.items():
            if value == 1:
                sum = sum + key
        return sum