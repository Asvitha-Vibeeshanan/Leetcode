class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        sum = 0
        n = len(piles)//3
        new_piles = piles[n:]
        for i in range(len(new_piles)):
            if i%2 == 0:
                sum = sum + new_piles[i]
        return sum