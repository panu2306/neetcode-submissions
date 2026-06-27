class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first solution => time complexity == m * logn
        
        row_len = len(matrix[0])
        matrix_len = len(matrix)

        def _binary_search(l, r, row): 
            while(l <= r):
                mid = (l + r) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target: 
                    l = mid + 1 
                else: 
                    r = mid - 1
            return False    

        for row in matrix:
            l = 0 
            r = row_len - 1 
            if(row[l] <= target <= row[r]): 
                return _binary_search(l, r, row)
        return False

        

             
