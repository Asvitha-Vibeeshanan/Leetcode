class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = list(str(num))
            res = res + num
        return list(map(int, res))