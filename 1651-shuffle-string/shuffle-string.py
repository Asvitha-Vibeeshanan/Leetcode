class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str_arr = [0]*len(indices)
        for i in range(0,len(indices)):
            str_arr[indices[i]] = s[i]
        return ''.join(str_arr)  