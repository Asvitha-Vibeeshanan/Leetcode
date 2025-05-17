class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in range(len(strs)):
            newstr = ''.join(sorted(strs[i]))
            if newstr not in dict:
                dict[newstr] = [strs[i]]
            else:
                dict[newstr].append(strs[i])
        res = []
        for d in dict:
            res.append(dict[d])
        return res