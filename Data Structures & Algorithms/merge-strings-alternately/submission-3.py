class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1),len(word2))
        output = ""
        for i in range(n):
            output += word1[i]
            output += word2[i]
        if len(word2) > n:
            output +=  word2[n:]
        else:
            output +=  word1[n:]
        return output
        
        