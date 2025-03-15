class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        res = []
        for i in range(len(A)):
            arr1.append(A[i])
            arr2.append(B[i])
            count = 0
            for j in range(len(arr1)):
                if arr1[j] in arr2:
                    count = count+1
            res.append(count)
        return res