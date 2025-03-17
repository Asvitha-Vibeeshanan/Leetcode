class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        temp = capacity
        for i in range(len(plants)):
            if plants[i] <= capacity:
                capacity = capacity - plants[i]
                steps = steps + 1
            else:
                capacity = temp
                capacity = capacity - plants[i]
                steps = steps + (i+1) + i
        return steps