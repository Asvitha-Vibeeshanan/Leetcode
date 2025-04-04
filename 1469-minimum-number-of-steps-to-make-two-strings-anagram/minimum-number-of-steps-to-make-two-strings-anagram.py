from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        total_steps = sum((count_s - count_t).values())
        return total_steps
        # count = 0
        # s = sorted(s)
        # t = sorted(t)
        # for char in s:
        #     if char in t:
        #         t.remove(char)
        #     else:
        #         count = count + 1
        # return count 