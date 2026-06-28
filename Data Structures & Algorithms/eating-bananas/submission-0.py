from math import ceil 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # First solution: brute force - takes -> P * max(P) => P == No. of Piles
        # min_rate = 1 
        # max_rate = max(piles)
        # # range of rate of bananas per hour => [min_rate, max_rate]
        # for rate in range(min_rate, max_rate + 1):
        #     total_hours = 0  
        #     for pile in piles:
        #         hours = ceil(pile/rate)
        #         total_hours += hours
        #         if total_hours > h: 
        #             break 
        #     if total_hours <= h: 
        #         return rate 

        # Second solution: use binary search for finding the correct rate: 

        def _calculate_hours(rate):
            total_hours = 0 
            for pile in piles: 
                total_hours += ceil(pile/rate)
            return total_hours 
        
        min_rate = 1 
        max_rate = max(piles)
        optimum_rate = max_rate 

        while min_rate <= max_rate: 
            mid_rate = (min_rate + max_rate) // 2 

            if _calculate_hours(mid_rate) <= h:
                optimum_rate = min(mid_rate, optimum_rate)
                max_rate = mid_rate - 1 
            else:
                min_rate = mid_rate + 1 

        return optimum_rate  

        
