from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(list) # row_map[row1_index] => [row1_items]
        col_map = defaultdict(list) # col_map[column1_index] => [column1_items]
        sub_box_map = defaultdict(list) # sub_box_map[sub_box_index] => [sub_box_elements]
        ignore_item = "."
        for row in range(9):
            for col in range(9):
                item = board[row][col]
                index = (row//3) * 3 + (col//3)
                if(item is ignore_item):
                    continue
                if(item in col_map[col] or item in row_map[row] or item in sub_box_map[index]):
                    return False
                col_map[col].append(item)
                row_map[row].append(item)
                sub_box_map[index].append(item)
        return True

            