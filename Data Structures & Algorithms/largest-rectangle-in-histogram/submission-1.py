class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped_index = stack.pop()
                if stack:
                    left_boundary = stack[-1]
                else:
                    left_boundary = -1
                width = i - left_boundary - 1
                area = max(area,heights[popped_index]*width)
            stack.append(i)
             
        while stack:
            popped_index = stack.pop()
            if stack:
                left_boundary = stack[-1]
            else:
                left_boundary = -1
            right_boundary = len(heights)
            width = right_boundary - left_boundary - 1
            area = max(area,heights[popped_index]*width)
        return area