from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        left = 0
        substring = set()
        for right in range(len(s)):
            while(s[right] in substring):
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            longest_length = max(len(substring), longest_length)
        return longest_length 
