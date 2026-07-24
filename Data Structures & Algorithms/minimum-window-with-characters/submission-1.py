class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        k = len(t)
        if len(t)>len(s): 
            return ""
        for i in range(k):
            need[t[i]] = need.get(t[i],0)+1
        required = len(need)
        formed = 0
        window = {}
        min_len = float("inf")
        l = 0
        start = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            if s[r] in need and window[s[r]] == need[s[r]]:
                formed+=1
            while formed == required:
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    start = l
                window[s[l]]-=1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        if min_len == float("inf"):
            return ""
        return s[start : start + min_len]

