class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time complexity: O(2^N)
        res = []

        # array to build subsets 
        subset = []
        def dfs(i):
            if i >= len(nums):
                # subset is going to be modified, hence we add copies 
                res.append(subset.copy())
                return 

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision not to inclusde nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res 