class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l = l + 1 
            if nums[r] not in window:
                window.add(nums[r])
            else:
                return True
        return False
        # if len(nums) == 1:
        #     return False
        # if len(nums) == set(nums):
        #     return False
        # # if len(nums) <= k :
        # #     return True
        
        # dict = {}
        # for i in range(len(nums)):
        #     if nums[i] not in dict:
        #         dict[nums[i]] = [i]
        #     else:
        #         dict[nums[i]].append(i)
        # print(dict)


        # for key, values in dict.items():
        #     values = sorted(values, reverse = True)
        #     if len(values) >=2:
        #         if (values[0]-values[1]) <= k:
        #             return True
        #         else:
        #             return False
        #         # print(values)
        #     #     if(dict[nums[i]] <= k):
        #     #         return True
        #     # return False
        