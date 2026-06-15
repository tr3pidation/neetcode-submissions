class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        m = min(len(s) for s in strs)
        #check through jth letter of all elements 
        for j in range(m):
            prefix = strs[0][j]
            for i in range(len(strs)):
                if strs[i][j] != prefix:
                    return output
            output += prefix
        return output

            
                
            