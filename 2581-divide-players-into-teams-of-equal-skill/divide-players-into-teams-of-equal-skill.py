class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        res = 0
        l = 0
        r = len(skill)-1
        prev = skill[l] + skill[r]
        while(l<r):
            if prev == skill[l] + skill[r]:
                res = res + (skill[l] * skill[r])
                prev = skill[l] + skill[r]
                l = l+1
                r = r-1
            else:
                return -1
        return res      