class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(n * 2^n)
        res = []
        nums.sort()

        def backtrack(i, subset):
            # this is how we know we have gone through the entire array 
            if i == len(nums):
                res.append(subset[::])
                return 

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            # All subsets that don't include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)

        backtrack(0, [])
        return res 





        