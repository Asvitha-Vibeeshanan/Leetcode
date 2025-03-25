class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dict = {}
        arr2 = sorted(list(set(arr)))
        for i in range(len(arr2)):
            dict[arr2[i]] = i+1
        for i in range(len(arr)):
            arr[i] = dict[arr[i]]
        return arr 
        