class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first approach - sorting
        # nums.sort()
        # highest_count = curr_count = 1 
        # for i in range(1, len(nums)):
        #     if(nums[i-1] == nums[i]):
        #         continue
        #     elif(nums[i-1] + 1 == nums[i]):
        #         curr_count += 1
        #         highest_count = max(curr_count, highest_count)
        #     else:
        #         curr_count = 1
        # return highest_count

        # second approach - optimal - using set 
        hashset = set(nums)
        highest_count = 0
        for num in nums:
            if(num-1 in hashset):
                continue
            curr_count = 0
            while(num in hashset):
                num += 1
                curr_count += 1
            highest_count = max(highest_count, curr_count)
        return highest_count
        
    

        