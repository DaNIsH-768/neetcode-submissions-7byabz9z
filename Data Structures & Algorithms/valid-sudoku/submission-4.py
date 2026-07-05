class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {}
        colMap = {}

        # Check each row: if a number appears twice return false
        for i in range(len(board)):
            rowMap[i] = set()
            colMap[i] = set()
            for j in range(len(board[i])):
                if board[i][j] in rowMap[i]:
                    return False
                
                if board[i][j] != ".":
                    rowMap[i].add(board[i][j])
                
                # Check each col: if a number appears twice return false
                    
                if board[j][i] in colMap[i]:
                    return False
                
                if board[j][i] != ".":
                    colMap[i].add(board[j][i])
                    
        
        # Check each 9X9: if a numbers apperas twice return false
        row = 0
        col = 0
        block = 1

        block_map = {}

        while col <= 8 and row <= 8:
            block_map[block] = set()
            for i in range(row, row+3, 1):
                for j in range(col, col+3, 1):
                    if board[i][j] == ".":
                        continue

                    if board[i][j] in block_map[block]:
                        return False
                    
                    block_map[block].add(board[i][j])
            
            row += 3
            if row > 8:
                row = 0
                col += 3

        return True