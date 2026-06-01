class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0 
        l = 0 
        n = 0 
        for r in range(len(arr)):
            curr_sum += arr[r]
            if(r-l+1 == k):
                if(curr_sum / k >= threshold):
                    n += 1
                curr_sum -= arr[l]
                l = l + 1
        return n

        