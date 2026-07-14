class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            result[i] = nums[i-1] * result[i-1]
        rightProduct = 1
        for j in range(len(nums)-1,-1,-1):
            result[j] *= rightProduct
            rightProduct *= nums[j]
        return result