class Solution:
    def validPalindrome(self, s: str) -> bool:
        #helper function for after removing one character, optinise ispalindrome for lower letters
        def isPalindrome(self, s: str) -> bool:
            #try with lesser space
            left = 0
            right = len(s)-1
            while left < right: 
                if s[left] != s[right]:
                    return False
                #correct, keep moving on to check
                left +=1
                right -=1
            return True 
            
        left = 0
        right = len(s)-1
        while left<right:
            if s[left] != s[right]:
                if isPalindrome(self,s[left:right]) or isPalindrome(self,s[left+1:right+1]):
                    return True
                else:
                    return False
            left +=1
            right -=1 
        return True
        