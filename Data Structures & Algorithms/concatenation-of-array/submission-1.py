class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        #initialise 0s
        ans = nums + [0] * len(nums)
        n = len(nums)
        for i in range (n):
            ans[i + len(nums)] = nums[i]
        return ans