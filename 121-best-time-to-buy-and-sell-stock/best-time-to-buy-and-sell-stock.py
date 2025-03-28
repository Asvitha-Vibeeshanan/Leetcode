class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        max = 0
        while(r < len(prices)):
            if prices[l] > prices[r]:
                l = l+1
            else:
                if max < (prices[r] - prices[l]):
                    max = prices[r] - prices[l]
                r = r+1 
        return max