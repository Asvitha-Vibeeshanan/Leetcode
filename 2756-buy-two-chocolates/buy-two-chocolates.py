class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Sort the prices to find the two cheapest chocolates
        prices.sort()
        
        # If the sum of the two cheapest chocolates is greater than the available money, return money
        if prices[0] + prices[1] > money:
            return money
        
        # Otherwise, subtract the cost of the two cheapest chocolates from the money
        return money - (prices[0] + prices[1])
