class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        bucket = [[] for _ in range(len(nums)+1)]
        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1
        for num, freq in hashmap.items():
            bucket[freq].append(num)
        for i in range(len(bucket)-1,0,-1):
            for item in bucket[i]:
                result.append(item)
                if len(result) == k:
                    return result