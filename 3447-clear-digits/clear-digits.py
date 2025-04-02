class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        if s.isalpha():
            return s
        else:
            for i in range(len(s)):
                if s[i].isalpha():
                    stack.append(s[i])
                else:
                    stack.pop()
        return "".join(stack)              