class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        matrix = []

        num = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(num)
                num += 1
            matrix.append(row)
        i = 0
        j = 0
        for command in commands:
            if command == "RIGHT":
                j = j + 1
            elif command == "LEFT":
                j = j - 1
            elif command == "UP":
                i = i - 1
            else:
                i = i+1
            current_position = matrix[i][j]
        return current_position

