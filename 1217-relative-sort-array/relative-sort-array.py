class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        arr3 = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    arr.append(arr1[j])

        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                arr3.append(arr1[i])
        return arr+sorted(arr3)