class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # first approach - O(n^2): 
        # l = len(nums)
        # for i in range(l):
        #     for j in range(l):
        #         if(i != j and nums[j] == nums[i]):
        #             return True
        # return False
        # Second Approach - O(nlogn)
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if(nums[i] == nums[i+1]):
        #         return True
        # return False
        # # third approach - O(n) time and O(n) space
        hashset = set()
        for num in nums:
            if(num in hashset):
                return True
            hashset.add(num)
        return False

        

        