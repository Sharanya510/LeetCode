class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                mid = (left + right) // 2
                # print(pivot_idx, pivot_idx // n, pivot_idx % n)
                pivot_element = matrix[mid // n][mid % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = mid - 1
                    else:
                        left = mid + 1
        return False