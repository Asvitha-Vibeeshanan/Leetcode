class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr1, arr2, arr3 = [], [], []
        for num in nums:
            if num < pivot:
                arr1.append(num)
            if num > pivot:
                arr2.append(num)
            if num == pivot:
                arr3.append(num)
        return arr1+arr3+arr2