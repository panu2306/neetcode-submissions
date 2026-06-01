class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) - 1
        while(left < right):
            curr_area = (right - left) * min(heights[left], heights[right])
            if(heights[right] < heights[left]):
                right -= 1
            else:
                left += 1
            max_area = max(curr_area, max_area)
        return max_area

        