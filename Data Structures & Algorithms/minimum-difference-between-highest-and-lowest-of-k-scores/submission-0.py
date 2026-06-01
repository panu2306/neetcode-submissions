class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort() # [1,2,3,3,5,6]
        l, r = 0, k-1
        curr_diff = 0
        min_diff = float('inf')

        while(r < len(nums)):
            curr_diff = nums[r] - nums[l]
            min_diff = min(curr_diff, min_diff)
            l, r = l + 1, r + 1
        return min_diff

            

        
        