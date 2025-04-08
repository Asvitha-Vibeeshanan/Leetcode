class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
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
            current_position = i*n + j
        return current_position