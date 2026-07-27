class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for bracket in s:
            if bracket in bracket_map:
                if not stack or stack[-1] != bracket_map[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)

        return not stack