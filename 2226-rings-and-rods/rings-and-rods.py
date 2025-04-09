class Solution:
    def countPoints(self, rings: str) -> int:
        dict1 = {}
        rings = list(rings)
        for i in range(1,len(rings),2):
            if rings[i] not in dict1:
                dict1[rings[i]] = [rings[i-1]]
            else:
                dict1[rings[i]].append(rings[i-1])
        count = 0
        for key, value in dict1.items():
            if "B" in value and "G" in value and "R" in value:
                count = count + 1
        return count
