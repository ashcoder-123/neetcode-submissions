from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store[key]
        l = 0
        r = len(entries)-1
        while l <= r:
            mid = (l+r)//2
            if entries[mid][0] <= timestamp:
                l = mid+1
            else:
                r = mid-1
        if r >= 0:
            return entries[r][1]
        return ""


        
