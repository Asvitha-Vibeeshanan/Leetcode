class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_pointer = 0
        result = ""
        
        for k in key:
            if k not in dict and k != " ":
                dict[k] = alpha[alpha_pointer]
                alpha_pointer += 1
        
        for m in message:
            if m in dict:
                result += dict[m]
            if m == " ":
                result += " "
        return result