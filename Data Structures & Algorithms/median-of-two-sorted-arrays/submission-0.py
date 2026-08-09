class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if len(B) < len(A):
            A,B = B,A
        a = len(A)
        b = len(B)
        
        l = 0
        r = a
        while l<=r:
            partitionA = (l + r) // 2
            partitionB = (a + b + 1) // 2 - partitionA
            leftA = A[partitionA - 1] if partitionA > 0 else float('-inf')
            rightA = A[partitionA] if partitionA < a else float('inf')

            leftB = B[partitionB - 1] if partitionB > 0 else float('-inf')
            rightB = B[partitionB] if partitionB < b else float('inf')
            if leftA <= rightB and leftB <= rightA:
                left_max = max(leftA, leftB)
                right_min = min(rightA, rightB)
                if (a+b) % 2 == 0:
                    return (left_max+right_min) / 2
                else:
                    return left_max
            elif leftA > rightB:
                r = partitionA - 1
            else:
                l = partitionA + 1
