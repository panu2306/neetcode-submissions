class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0 
        total_sum = 0
        max_freq = 0
        for r in range(len(nums)):
            total_sum += nums[r]
            # The average of all the numbers when becomes equal to the target then that window is valid
            # target == total + k // window_length 
        
            # for invalid window, shift left pointer to right
            while((r -l + 1) * nums[r] > total_sum + k):
                total_sum -= nums[l]
                l += 1
            max_freq = max(r - l + 1, max_freq)
        return max_freq

        