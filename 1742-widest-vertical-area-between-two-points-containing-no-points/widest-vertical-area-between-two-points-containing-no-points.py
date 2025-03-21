class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, reverse = True)
        diff = 0
        i = 0
        max = 0
        while(i<len(points)-1):
            diff = points[i][0] - points[i+1][0]
            if max < diff:
                max = diff
            i += 1
        return max 

        