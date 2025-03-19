class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = str(bank[0]).count('1')
        for i in range(1,len(bank)):
            count_1 = str(bank[i]).count('1')
            if count_1 != 0:
                res = res + (prev * count_1)
                prev = count_1
        return res