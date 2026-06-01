from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        # {
        #     ("act") => ["act", "cat"], 
        #     ("aht") => ["hat"], 
        #     ("opst") => ["stop", "pots", "tops"]
        # }
        
         
        for string in strs: 
            char_array = [0] * 26
            for c in string:
                char_array[ord(c) - ord('a')] += 1 
            result[tuple(char_array)].append(string)
        return list(result.values())
                 
                



        
        