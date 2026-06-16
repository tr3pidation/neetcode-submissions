class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create clean array first
        clean = ""
        for char in s:
            if char.isalnum():
                # add uncapitalised
                clean += char.lower()

        left = 0
        right = len(clean) -1
        while left<right:
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1
        return True

        