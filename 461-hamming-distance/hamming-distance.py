class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x^y
        n = int(bin(diff)[2:],2)
        return n.bit_count()