class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # last valid element of nums1
        j = n - 1 # last valid element of nums2
        k = m + n - 1 # last element of nums1
        while i >= 0 and j>=0:
            # if not higher, shift
            if nums2[j]<nums1[i]:
                nums1[k] = nums1[i]
                i-=1 #move down to next value of nums1
            else: #if higher, insert, no shift
                nums1[k] = nums2[j] 
                j-=1 #remain at same value of nums1
            k-=1
        # check if j more than 0, then reduce j and k since i is already 0 or -1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
            
        

            
        