class Solution:
    def countAndSay(self, n: int) -> str:
        # Time Complexity: O(2^n)

        def helper(s):
            result = ""
            count = 1
            for i in range(len(s)):
                if i == len(s) - 1 or s[i] != s[i+1]:
                    result += str(count) + s[i]
                    count = 1
                else:
                    count += 1 
            return result

        ans = "1"
        for i in range(2, n+1):
            ans = helper(ans)
        return ans 