class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while(n):
            product = product * (n%10)
            sum = sum + (n%10)
            n = n//10
        return product - sum   