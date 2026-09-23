from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowc = defaultdict(set)
        colc = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowc[r] or board[r][c] in colc[c] or board[r][c] in square[(r//3,c//3)]):
                    return False
                
                rowc[r].add(board[r][c])
                colc[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True

