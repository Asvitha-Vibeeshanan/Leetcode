class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1 = 0
        count2 = 0
        n = len(s)//2
        string1 = s[:n]
        string2 = s[n:]
        for i in range(len(string1)):
            if string1[i].lower() == "a" or string1[i].lower() == "e" or string1[i].lower() == "i" or string1[i].lower() == "o" or string1[i].lower() == "u":
                count1 = count1 + 1
            if string2[i].lower() == "a" or string2[i].lower() == "e" or string2[i].lower() == "i" or string2[i].lower() == "o" or string2[i].lower() == "u":
                count2 = count2 + 1
        
        return count1 == count2