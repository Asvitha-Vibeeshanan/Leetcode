class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            result = 0
        if divisor > 0 and dividend > 0:
            result =  dividend//divisor
        if divisor < 0 and dividend > 0:
            result = (-(dividend//abs(divisor)))
        if divisor > 0 and dividend < 0:
            result = (-(abs(dividend)//(divisor)))
        if divisor < 0 and dividend < 0:
            result = (abs(dividend)//abs(divisor))
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
