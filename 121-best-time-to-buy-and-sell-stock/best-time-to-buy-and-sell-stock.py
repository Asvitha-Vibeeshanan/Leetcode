class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        max = 0
        while(r < len(prices)):
            if prices[l] > prices[r]:
                l = l+1
            else:
                diff = prices[r] - prices[l]
                if max < diff:
                    max = diff
                r = r+1 
        return max