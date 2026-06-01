class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first approach - O(nlogn)
        # return sorted(s) == sorted(t)

        # second approach - O(n) - Optimal for interview
        if(len(s) != len(t)):
            return False
        hashmap = {}
        for c in s:
           hashmap[c] = hashmap.get(c, 0) + 1
        for c in t:
            if(c not in hashmap):
                return False
            hashmap[c] -= 1
            if(hashmap[c] < 0):
                return False
        return True

        # third approach - pythonic collection import 
        # from collections import Counter
        # return Counter(s) == Counter(t)

        # fourth approach - using character array and ord
        # if(len(s) != len(t)):
        #     return False
        
        # count = [0] * 26

        # for i in range(len(s)):
        #     count[ord(s[i]) - ord('a')] += 1
        #     count[ord(t[i]) - ord('a')] -= 1
        # for i in range(26):
        #     if count[i] != 0: 
        #         return False
        # return True


        