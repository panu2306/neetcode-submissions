class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #First Approach - using sorted 
        # hashmap = {}
        # for s in strs: 
        #     sorted_s = ''.join(sorted(s))
        #     if(sorted_s not in hashmap):
        #         hashmap[sorted_s] = []
        #     hashmap[sorted_s].append(s)
        # return list(hashmap.values())
        # Second Approach - Optimal 
        hashmap = {}
        for s in strs:
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if(key not in hashmap):
                hashmap[key] = []
            hashmap[key].append(s)     
        return list(hashmap.values())