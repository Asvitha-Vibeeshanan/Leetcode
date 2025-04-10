class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = str(num)
            num = list(num)
            res = res + num
        return list(map(int, res))