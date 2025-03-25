class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        res = 0
        product = 1
        l = 0
        r = len(skill)-1
        prev = skill[l] + skill[r]
        while(l<r):
            # sum = skill[l] + skill[r]
            if prev == skill[l] + skill[r]:
                sum = skill[l] + skill[r]
                product = skill[l] * skill[r]
                res = res + product
                prev = sum
                l = l+1
                r = r-1
            else:
                return -1
        return res      