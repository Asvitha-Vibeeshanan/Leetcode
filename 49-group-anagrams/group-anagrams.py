class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            sorted_key = "".join(sorted(s))  
            if sorted_key not in dict:
                dict[sorted_key] = [s]
            else:
                dict[sorted_key].append(s)
        arr = []
        for d in dict:
            arr.append(dict[d])
        return arr