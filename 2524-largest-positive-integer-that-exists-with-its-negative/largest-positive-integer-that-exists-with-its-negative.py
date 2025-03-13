class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        arr = []
        arr1 = [abs(nums[i]) for i in range(len(nums)) if nums[i]<0]
        arr2 = [nums[i] for i in range(len(nums)) if nums[i]>0]
        print(arr1)
        print(arr2)
        return max(list(set(arr1)&set(arr2))) if list(set(arr1)&set(arr2)) else -1
        print()
        dict1 = {}
        dict2 = {}
        for num in nums:
            if num < 0:
                if abs(num) not in dict1:
                    dict1[num] = 1
                else:
                    dict1[num] += 1
            else:
                if num not in dict2:
                    dict2[num] = 1
                else:
                    dict2[num] += 1
        for key, value in dict1.items():
            if abs(key) in dict2:
                arr.append(abs(key))
        return max(arr) if arr else -1