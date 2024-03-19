class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                # cur.copy() because we are going to continue using this variable 
                res.append(cur.copy())
                return res 
            
            # edge cases 
            if i >= len(candidates) or total > target:
                return 

            cur.append(candidates[i])
            # below i stays the same because we are not restricting which candidates we are allowed to choose 
            dfs(i, cur, total + candidates[i])
            # we have to pop the current before we go down the other decision 
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res 