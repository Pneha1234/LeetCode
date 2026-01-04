class Solution:
    def solve(self, board) :
        """
        Do not return anything, modify board in-place instead.
        """
        row, column = len(board), len(board[0])
        visited = [[False]* column for _ in range(row)]

        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= column or board[r][c]!='O' or visited[r][c]:
                return
            visited[r][c]=True
            # check in all direction
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # check the row level boundary that is row=0 and row=row-1:
        for c in range(column):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[row-1][c] == 'O':
                dfs(row-1,c)
         
        # check for boundary level column where column=0 and column-1
        for r in range(row):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][column-1] == 'O':
                dfs(r, column-1)

        for r in range(row):
            for c in range(column):
                if board[r][c] == 'O' and not visited[r][c]:
                    board[r][c] = 'X'