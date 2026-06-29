class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] == target: 
                return mid 
            
            # first half is sorted
            if nums[l] <= nums[mid]:
                if target < nums[l]:
                    l = mid + 1 
                elif target > nums[mid]: 
                    l = mid + 1 
                else: 
                    r = mid - 1  
            # second half is sorted
            # [6, 1, 2, 3, 4, 5]
            else:
                if target < nums[mid]:
                    r = mid - 1 
                elif target > nums[r]: 
                    r = mid - 1 
                else: 
                    l = mid + 1
        return -1  



             


        