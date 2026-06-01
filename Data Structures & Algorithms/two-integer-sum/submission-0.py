class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # First Approach - O(n^2) brute-force approach:
        # l = len(nums)
        # for i in range(l):
        #     for j in range(i+1, l):
        #         if(nums[i] + nums[j] == target):
        #             return [i, j]

        # Second Approach - O(n) => Optimal for interviews
        hashmap = {}
        for i in range(len(nums)):
            if((target - nums[i]) in hashmap):
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
        
        # Third Approach - sort and two pointer
        # nums_with_index = [(num, index) for index, num in enumerate(nums)]
        # ptr1, ptr2 = 0, len(nums) - 1
        # while(ptr1 < ptr2):
        #     current_sum = nums_with_index[ptr1][0] + nums_with_index[ptr2][0]
        #     if(current_sum == target):
        #         return [nums_with_index[ptr1][1], nums_with_index[ptr2][1]]
        #     elif(current_sum < target):
        #         ptr1 += 1 
        #     else: 
        #         ptr2 -= 1
        # return []
            




