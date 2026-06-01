class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        s2_count = [0] * 26
        s1_len = len(s1)
        s2_len = len(s2)

        if(s1_len > s2_len):
            return False

        for i in range(s1_len):
            s1_count[ord(s1[i]) - ord('a')] += 1
        
        def compare_arrays(s1, s2):
            for i in range(26):
                if(s1[i] != s2[i]):
                    return False
            return True
        l = 0
        for r in range(s2_len):
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if(r-l+1 == s1_len):
                result = compare_arrays(s1_count, s2_count)
                if result: 
                    return True
                index = ord(s2[l]) - ord('a')
                s2_count[index] -= 1 
                l += 1
        return False

            
            

            

        