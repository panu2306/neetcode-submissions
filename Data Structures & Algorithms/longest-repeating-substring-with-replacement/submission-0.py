class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        max_freq = 0
        hashmap = {}
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            max_freq = max(max_freq, hashmap[s[r]])
            while((r-l) - max_freq >= k):
                hashmap[s[l]] -= 1
                l += 1
            

            max_len = max(max_len, r-l+1)
        return max_len        