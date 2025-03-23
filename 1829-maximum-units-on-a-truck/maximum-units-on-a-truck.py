class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        total = 0
        res = 0
        for i in range(len(boxTypes)):
            if total + boxTypes[i][0] <= truckSize:  
                total += boxTypes[i][0]
                res += (boxTypes[i][0] * boxTypes[i][1])
            else:
                remaining_space = truckSize - total  
                res += (remaining_space * boxTypes[i][1])
                break  
        return res  