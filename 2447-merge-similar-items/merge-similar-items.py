class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        arr = []
        dict = {}
        for i in items1:
            if i[0] not in dict:
                dict[i[0]] = i[1]
        for i in items2:
            if i[0] in dict:
                dict[i[0]] += i[1]
            else:
                dict[i[0]] = i[1]
        for i,j in dict.items():
            arr.append([i,j])
        arr.sort()
        return arr