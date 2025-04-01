class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]
        for i in range(0,len(gain)):
            arr.append(gain[i] + arr[len(arr)-1])
        return max(arr)