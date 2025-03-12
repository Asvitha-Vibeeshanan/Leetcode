class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        word3 = ''
        if len(word1) == len(word2):
            while(len(word1)!= l and len(word2)!= r):
                word3 = word3 + word1[l] + word2[r]
                l = l+1
                r = r+1
            return word3

        else:
            while(len(word1)!= l and len(word2)!= r):
                word3 = word3 + word1[l] + word2[r]
                l = l+1
                r = r+1
            if len(word1) > len(word2):
                return word3+word1[len(word2):]
            else:
                return word3+word2[len(word1):]
    
    