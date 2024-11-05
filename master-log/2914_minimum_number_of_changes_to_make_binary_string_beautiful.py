class Solution:
    def minChanges(self, s: str) -> int:
        length = len(s)
        result = 0        
        i = 0
        while i < length-1:
            if s[i]!=s[i+1]:
                result += 1
            i+=2            
        return(result)
           
s = "1111"
print(Solution().minChanges(s))