class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First Approach - Brute Force
        # freq_array = []
        # ele_tracker = []
        # l = len(nums) 
        # prev_count = 0
        # for i in range(l):
        #     if(nums[i] not in ele_tracker):
        #         ele_tracker.append(nums[i])
        #         count = 0
        #         for j in range(i+1, l):
        #             if(nums[i] == nums[j]):
        #                 count += 1
        #     if(count > prev_count):
        #         freq_array.append(nums[i])
        #         prev_count = count
        # return freq_array

        # Second Approach - Optimal
        l = len(nums)
        bucket = [[] for i in range(l+1)]
        hashmap = {}
        output = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1 
        for key, val in hashmap.items():
            bucket[val].append(key)
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                output.append(n)
                if(len(output) == k):
                    return output

             


        