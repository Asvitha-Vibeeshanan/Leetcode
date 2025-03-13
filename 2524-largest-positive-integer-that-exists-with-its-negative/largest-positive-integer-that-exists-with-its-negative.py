class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        arr = []
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

        print(dict1)
        print(dict2)

        for key, value in dict1.items():
            if abs(key) in dict2:
                arr.append(abs(key))
        return max(arr) if arr else -1