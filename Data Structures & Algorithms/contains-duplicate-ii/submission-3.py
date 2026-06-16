class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = {}
        for i in range(len(nums)):
            num = nums[i]
            #check if key in record
            if num in record:
                #check if value - index within range
                if i - record[num] <= k:
                    return True
            record[num] = i
            #record value num for key i, or update if needed
        return False
            
            

        