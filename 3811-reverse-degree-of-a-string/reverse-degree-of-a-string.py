class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        for i in range(0,len(s)):
            position = (i+1) * (26 - (ord(s[i]) - ord('a')))
            sum = sum + position
        return sum  