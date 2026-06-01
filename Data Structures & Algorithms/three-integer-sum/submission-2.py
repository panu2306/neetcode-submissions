class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        output = []
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        for i in range(l):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            j, k = i + 1, l-1
            while(j < k):
                threesum = nums[i] + nums[j] + nums[k] 
                if(threesum == 0):
                    output.append([nums[i],nums[j], nums[k]])
                    j += 1
                    while(nums[j] == nums[j-1] and j < k):
                        j += 1
                elif(threesum < 0):
                    j += 1
                else: 
                    k -= 1
        print(output)
        return output 
         