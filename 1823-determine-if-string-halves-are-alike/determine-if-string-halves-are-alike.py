class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count1 = 0
        count2 = 0
        n = len(s)//2
        string1 = s[:n]
        string2 = s[n:]
        for i in range(n):
            if string1[i] in arr:
                count1 = count1 + 1
            if string2[i] in arr:
                count2 = count2 + 1
        return count1 == count2