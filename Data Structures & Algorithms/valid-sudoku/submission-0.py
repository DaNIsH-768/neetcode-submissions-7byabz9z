class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {}
        colMap = {}

        # Check each row: if a number appears twice return false
        for i in range(len(board)):
            rowMap[i] = []
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                    
                if board[i][j] in rowMap[i]:
                    return False
                
                rowMap[i].append(board[i][j])

        # Check each col: if a number appears twice return false
        for i in range(len(board)):
            colMap[i] = []
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                    
                if board[j][i] in colMap[i]:
                    return False
                
                colMap[i].append(board[j][i])
        
        # Check each 9X9: if a numbers apperas twice return false
        row = 0
        col = 0
        block = 1

        block_map = {}

        while col <= 8 and row <= 8:
            block_map[block] = []
            for i in range(row, row+3, 1):
                for j in range(col, col+3, 1):
                    if board[i][j] == ".":
                        continue

                    if board[i][j] in block_map[block]:
                        return False
                    
                    block_map[block].append(board[i][j])
            
            row += 3
            if row > 8:
                row = 0
                col += 3

        return True