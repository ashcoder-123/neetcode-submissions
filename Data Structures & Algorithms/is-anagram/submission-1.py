class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for char in s:
            hashmap[char] = hashmap.get(char,0)+1
        for char in t:
            hashmap[char] = hashmap.get(char,0)-1
        return all(value == 0 for value in hashmap.values())

    
        