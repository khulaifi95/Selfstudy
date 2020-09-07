class Solution:
    def binarySearch(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical:
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True

        return False

    def search2dMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binarySearch(matrix, target, i, True)
            horizontal_found = self.binarySearch(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True

        return False