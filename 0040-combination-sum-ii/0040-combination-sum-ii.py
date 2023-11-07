class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #Time Complexity: O(2^n)
        candidates.sort()
        res = []
         
        
        #here target will be the target we are planning to sum upto because every time we add the target will change 
        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy()) #copy() bcz cur is going to change every time 
            if target <= 0:
                return 
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i+1, target-candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack([], 0, target) 
        return res
    