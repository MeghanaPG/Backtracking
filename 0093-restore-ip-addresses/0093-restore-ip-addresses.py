class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Backtracking 
        # adding 4 periods (3/2/1 digits before or after each period)
        res = []
      
        if len(s) > 12:
            return res

        def backtrack(i, dots, curIp):
            if dots == 4 and i == len(s):
                # we don't want the last dot 
                res.append(curIp[:-1])
                return 
            if dots > 4:
                return 
            
            # min because we might have just 2 digits left in the S
            for j in range(i, min(i+3,len(s))):
                # if we have 0 then the length of that part of ip has to be 1 or it can't have a leading 0
                # if int(s[i:j+1]) < 256 and (i == j and s[i] != "0"):
                if int(s[i:j+1]) <= 255 and (s[i] != "0" or len(s[i:j+1]) == 1):

                    backtrack(j+1, dots+1, curIp + s[i:j+1] + ".")
        
        backtrack(0,0,"")
        return res 
            


     

            
