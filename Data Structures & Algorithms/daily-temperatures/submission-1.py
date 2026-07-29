class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length_of_temperatures = len(temperatures)
        result = [0] * length_of_temperatures
        stack = []
        for index in range(length_of_temperatures):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                previous_index = stack[-1]
                result[previous_index] = index - previous_index
                stack.pop()
            stack.append(index)
        return result