class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left = [1, 1, 2, 8]
        # right = [48,24,6,1]
        l = len(nums)
        output = [1] * l
        prefix = postfix = 1 
        for i in range(0, l):
            output[i] = prefix
            prefix *= nums[i] 
        # output at this point = [1, 1, 2, 8]
        for i in range(l-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        # output at this point = [48,24,12,8]
        return output

        