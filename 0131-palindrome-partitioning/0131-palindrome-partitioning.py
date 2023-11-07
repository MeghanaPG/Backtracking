class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # Base case 
            if i >= len(s):
                res.append(part.copy())
                return 
            
            # we have to check the substring 
            for j in range(i, len(s)):
                # check if we have the palindrome 
                if self.isPalindrome(s, i,j):
                     part.append(s[i:j+1])
                     dfs(j+1)
                     part.pop()
        dfs(0)
        return res 

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False 
            l, r = l+1, r-1
        return True 

               
        
