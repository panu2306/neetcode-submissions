class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        min_count = k
        curr_count = 0
        for r in range(len(blocks)):
            if(blocks[r] == 'W'):
                curr_count += 1
            if(r-l+1 == k):
                min_count = min(min_count, curr_count)
                if(blocks[l] == 'W'):
                    curr_count -= 1
                l += 1
        return min_count


                


