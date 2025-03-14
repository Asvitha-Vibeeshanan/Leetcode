class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = 0
        arr = [0] * len(pref)
        for i in range(len(pref)):
            if i == 0:
                arr[i] = pref[i]
            else:
                arr[i] = pref[i-1] ^ pref[i] 
        return arr
            
        