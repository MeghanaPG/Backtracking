class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Rough Time complexity: O(m * n * 4^len(word))
        rows,cols = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True 
            
            # edge case 
            if(r<0 or c<0 or r>=rows or c >=cols 
            or word[i] != board[r][c] or (r,c) in path):
                return False

            # if none of the above cases then the path has the right letter of the word that we are looking for 
            path.add((r,c))

            # we look for all 4 directions 
            res = (dfs(r + 1, c, i+1) or  
                    dfs(r - 1, c, i+1) or
                    dfs(r, c+1, i+1) or 
                    dfs(r, c-1, i+1))
            path.remove((r,c))
            return res 
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        return False 
