class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        m = min(len(s) for s in strs)
        #check through jth letter of all elements 
        for j in range(m):
            #prefix is the jth letter of the first word
            prefix = strs[0][j]
            for i in range(len(strs)):
                #stopping criteria if mismatch
                if strs[i][j] != prefix:
                    return output
            output += prefix
        #return when loop has been completed
        return output

            
                
            