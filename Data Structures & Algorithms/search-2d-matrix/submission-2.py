class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # first solution => time complexity == m * logn
        
        # row_len = len(matrix[0])
        # matrix_len = len(matrix)

        # def _binary_search(l, r, row): 
        #     while(l <= r):
        #         mid = (l + r) // 2
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] < target: 
        #             l = mid + 1 
        #         else: 
        #             r = mid - 1
        #     return False    

        # for row in matrix:
        #     l = 0 
        #     r = row_len - 1 
        #     if(row[l] <= target <= row[r]): 
        #         return _binary_search(l, r, row)
        # return False

        # second solution => time complexity == log m + long n == log(m*n)
        """
        In the first solution what we did is we iterated through each row of matrix and then 
        applied the binary search on each row. But the question also mentions the second
        condition => First integer of every row is greater than the last integer of the previous
        row which really means that the whole matrix is in ascending order. Therefore, 
        we can use binary search to the whole matrix and not only per row. We can use binary search
        to find the row itself in which the elements might be present (uses log m) and then apply binary 
        search to that row (use log n)
        """
        row_len, matrix_len = len(matrix[0]), len(matrix)

        start_row = 0
        end_row = matrix_len - 1 

        while start_row <= end_row: 
            mid_row = (start_row + end_row) // 2 

            if target < matrix[mid_row][0]: 
                end_row = mid_row - 1 
            elif target > matrix[mid_row][-1]:
                start_row = mid_row + 1
            else: 
                break 
        if not start_row <= end_row: 
            return False
            
        start, end = 0, row_len - 1
        while start <= end: 
            mid = (start + end) // 2 
            if target == matrix[mid_row][mid]: 
                return True 
            elif target < matrix[mid_row][mid]: 
                end = mid - 1
            else: 
                start = mid + 1 
        return False







             
