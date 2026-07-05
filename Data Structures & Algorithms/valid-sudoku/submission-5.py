class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {}
        colMap = {}
        blockMap = defaultdict(set)

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
      
                if board[i][j] in blockMap[(i//3, j//3)]:
                    return False
                
                if board[i][j] != ".":
                    blockMap[(i//3, j//3)].add(board[i][j])
                    
        return True