class Solution:
    def __init__(self):
        self.solution = []
        self.solutionFound = False 

    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        
        moves = [[-2,-1], [-2,1], [2,-1], [2,1], [1,2], [-1,-2], [1,-2], [-1,2]]

        visited = [[26] * n for _ in range(m)]

        def dfs_backtracking(r, c, visited, move):
            if move == m * n:
                self.solution, self.solutionFound = [row[:] for row in visited], True 
            
            for dr, dc in moves:
                newR, newC = r+dr, c+dc
                if 0 <= newR <= m-1 and 0 <=newC <= n - 1 and visited[newR][newC] == 26:
                    visited[newR][newC] = move 
                    dfs_backtracking(newR, newC, visited, move+1)
                    if self.solutionFound:
                        return
                    visited[newR][newC] = 26 
        visited[r][c] = 0 
        dfs_backtracking(r, c, visited, 1)

        return self.solution