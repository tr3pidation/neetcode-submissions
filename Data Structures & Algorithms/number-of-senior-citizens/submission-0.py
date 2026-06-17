class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sum = 0 
        for detail in details:
            if int(detail[-4]+detail[-3]) > 60:
                sum +=1
        return sum