class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        lst=[]
        di={}
        for i in items1:
            if i[0] not in di:
                di[i[0]]=i[1]
        for i in items2:
            if i[0] in di:
                di[i[0]]+=i[1]
            else:
                di[i[0]]=i[1]
        for i,j in di.items():
            lst.append([i,j])
        lst.sort()
        return lst