class Solution:
    def countPoints(self, rings: str) -> int:
        # dict1 = {}
        # for i in range(1, len(rings), 2):
        #     rod = rings[i]
        #     color = rings[i-1]
        #     if rod not in dict1:
        #         dict1[rod] = set()
        #     dict1[rod].add(color)
        
        # count = 0
        # for colors in dict1.values():
        #     if {"B", "G", "R"}.issubset(colors):
        #         count += 1
        
        # return count

        dict1 = {}
        rings = list(rings)
        for i in range(1,len(rings),2):
            if rings[i] not in dict1:
                dict1[rings[i]] = {rings[i-1]}
            else:
                dict1[rings[i]].add(rings[i-1])
        count = 0
        for colors in dict1.values():
            if {"B", "G", "R"}.issubset(colors):
                count += 1
        
        return count