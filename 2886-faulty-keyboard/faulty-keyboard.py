class Solution:
    def finalString(self, s: str) -> str:
        while(s.find("i") > 0):
            i = s.find("i")
            sub = s[:i]
            s = sub[::-1] + s[i+1:] 
        return s