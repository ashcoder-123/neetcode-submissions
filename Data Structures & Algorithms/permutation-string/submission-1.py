class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        k = len(s1)
        if len(s1)>len(s2): 
            return False
        for i in range(k):
            need[s1[i]] = need.get(s1[i],0)+1
        window = {}
        for j in range(k):
            window[s2[j]] = window.get(s2[j],0)+1
        if window == need:
            return True
        l = 0
        for r in range(k,len(s2)):
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l+=1
            window[s2[r]] = window.get(s2[r],0)+1
            if window == need:
                return True
        return False  
          