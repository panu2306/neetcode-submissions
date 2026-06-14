class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for index, temp in enumerate(temperatures): 
            count = 0
            curr_index = index 
            while curr_index < len(temperatures) and temperatures[curr_index] <= temp: 
                curr_index += 1 
                count += 1 
            if curr_index >= len(temperatures):
                count = 0
            result.append(count) 
        return result

        