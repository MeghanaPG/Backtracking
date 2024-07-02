class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Time Complexity: O(2^9) 
        # Backtracking 
        res = []

        def backtrack(start, curr, total):
            if total == n and len(curr) == k:
                res.append(curr.copy())
                return res 
            
            # edge cases 
            if len(curr) > k or total > n:
                return 
            
            for i in range(start, 10):
                curr.append(i)
                backtrack(i+1, curr, total + i)
                # reset 
                curr.pop()
    

        backtrack(1, [], 0)
        return res 
