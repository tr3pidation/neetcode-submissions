class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            check_list = arr[i+1:]
            #now check for highest number within check_list
            highest = check_list[0]
            for j in range(1, len(check_list)):
                if check_list[j] > highest:
                    highest = check_list[j]
            #update array
            arr[i] = highest
        arr[-1] = -1
        return arr        