from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_1 = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in dict_1:
                dict_1[key].append(string)
            else:
                dict_1[key] = [string]
        return [val for val in dict_1.values()]
        