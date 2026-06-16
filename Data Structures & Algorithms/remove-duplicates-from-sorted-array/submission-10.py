class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 1
        while right < len(nums):
            if nums[right] == nums[right-1]:
                #same value, move right
                right += 1
            else: #match, replace left, shift left and right 
            
                nums[left] = nums[right]
                left +=1
                right+= 1
        return left
            


        