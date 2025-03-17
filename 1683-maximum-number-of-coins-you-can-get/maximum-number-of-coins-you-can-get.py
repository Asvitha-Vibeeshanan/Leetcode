class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        sum = 0
        new_piles = piles[len(piles)//3:]
        print(new_piles)
        for i in range(0,len(new_piles),2):
            sum = sum + new_piles[i]
        return sum