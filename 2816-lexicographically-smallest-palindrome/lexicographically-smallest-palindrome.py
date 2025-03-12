class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        l = 0
        r = len(s) - 1
        s = list(s)
        while(l < r):
            if s[l] > s[r]:
                s[l] =s[r]
            else:
                s[r] = s[l]
            r = r-1
            l = l+1
            
        return ''.join(s)


        
            


        