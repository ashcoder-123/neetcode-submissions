class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map ={"{":"}","[":"]","(":")"} 
        for bracket in s:
            if bracket in bracket_map:
                stack.append(bracket)
            elif stack == []:
                return False
            elif bracket == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return True if stack == [] else False
            

        