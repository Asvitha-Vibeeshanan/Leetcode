class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_time = 0
        for house in garbage:
            total_time += len(house)
        last_M = last_G = last_P = 0
        for i in range(len(garbage)):
            if 'M' in garbage[i]:
                last_M = i
            if 'G' in garbage[i]:
                last_G = i
            if 'P' in garbage[i]:
                last_P = i
        sum = [0] * len(garbage)
        for i in range(1, len(garbage)):
            sum[i] = sum[i-1] + travel[i-1]
        total_time += sum[last_M]
        total_time += sum[last_G]
        total_time += sum[last_P]

        return total_time