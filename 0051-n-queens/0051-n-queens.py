class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() #(r+c) because it remains constant 
        negDiag = set() #(r-c) because it remains constant 

        res = []
        board = [["."] * n for i in range(n)]

        # we are gonna go row by row 
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                # if there is already a queen placed in that col or if the positive or the negative diagonal has been already filled, then we cannot place anything in this place  
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue 
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                # we are backtracking to see if multiple solutions exist 
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res 
