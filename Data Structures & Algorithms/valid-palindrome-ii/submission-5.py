class Solution:
    def validPalindrome(self, s: str) -> bool:
        #use left and right
        def isPalindrome(self, s: str) -> bool:
            #try with lesser space
            left = 0
            right = len(s)-1
            while left < right: 
                while left<right and not s[left].isalnum():
                    #if left is not alphanumeric, keep skipping to next alpha numeric
                    left +=1
                while left<right and not s[right].isalnum():
                    #if right is not alphanumeric, keep skipping to next alpha numeric
                    right -=1
                if s[left].lower() != s[right].lower():
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
        