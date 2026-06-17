class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #easier to solve in sorted
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            #bypass duplicates in SORTED ARRAY for first item
            if i > 0 and num == nums[i-1]: #check previous value same
                continue #bypass
            l,r = i+1,len(nums)-1
            while l<r:
                value = num + nums[l] + nums[r]
                if value > 0:
                    r -=1
                elif value < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    r-=1
                # bypass for repeated nums[l] and nums[r]
                    while nums[r+1] == nums[r] and l<r:
                        r-=1
        return res
            



        