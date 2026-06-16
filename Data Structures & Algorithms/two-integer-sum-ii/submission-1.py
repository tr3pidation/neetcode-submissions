class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) -1
        #array is sorted so just keep increasing and decreasing index1 and 2 accordingly
        while index1 < index2:
            current = numbers[index1] + numbers[index2]
            if current == target:
                return [index1+1,index2+1]
            elif current <= target:
                #smaller than target, increase index1
                index1 += 1
            else:
                index2 -=1
            




        
        