class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join((st for st in s if st.isalnum()))
        final = clean.lower()
        i = 0
        j = len(final)-1
        while i < j:
            if final[i] == final[j]:
                i+=1
                j-=1
                if i == len(final)/2:
                    return True
            else:
                return False
        return True