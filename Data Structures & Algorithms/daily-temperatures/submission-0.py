class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append([n, i])
        return res
            


        