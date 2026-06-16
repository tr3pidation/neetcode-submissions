class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        running = []
        for char in operations:
        
            if char == '+':
                running.append(running[-1]+ running[-2])
            elif char == 'C':
                running.pop()
            elif char == "D":
                running.append(2*running[-1])
            else:
                running.append(int(char))
        return sum(running)

            
        