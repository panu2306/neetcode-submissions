class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        count = 0
        for operation in logs: 
            if(operation == "./"):
                continue
            elif(operation == "../"):
                if count > 0:
                    count -= 1
            else:
                count += 1
        return count
            
            
        
        
        