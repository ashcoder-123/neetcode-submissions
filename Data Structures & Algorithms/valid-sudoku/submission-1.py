from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                num = board[row][col]
                box = (row//3,col//3)
                if (num in rows[row] or num in cols[col] or num in boxes[box]):
                    return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[box].add(num)
        return True
        