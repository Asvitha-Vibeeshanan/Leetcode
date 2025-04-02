class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            sum = 0
            while(num):
                digit = num % 10
                num = num //10
                sum = sum + digit
            arr.append(sum)
        return min(arr)
                
        