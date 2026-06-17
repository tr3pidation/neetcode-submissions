class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        highest = 0
        for num in nums:
            if not num:
                count = 0
            else:
                count += 1
            if count > highest:
                highest = count
        return highest
        