class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l=0
        maxfreq = 0
        maxLength = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1
            maxfreq = max(maxfreq,freq[s[r]])
            while (r-l+1) - maxfreq > k:
                freq[s[l]]-=1
                l+=1
            maxLength = max(maxLength, r-l+1)
        return maxLength


        