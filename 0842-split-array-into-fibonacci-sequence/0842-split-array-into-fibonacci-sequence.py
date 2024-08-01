class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)

        def backtrack(i):
            if i == n:
                return len(res) >= 3
            cur = 0 
            for j in range(i,n):
                if j > i and num[i] == "0":
                    break
                cur = cur * 10 + ord(num[j]) - ord('0')
                if cur >= 2 ** 31:
                    break
                if len(res) < 2 or cur == res[-2] + res[-1]:
                    res.append(cur)
                    if backtrack(j+1):
                        return res
                    res.pop()
            return False
        res = []
        backtrack(0)
        return res

            
