class Solution:
    def word_search(self, matrix: list, word: str) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if word is None or len(word) == 0:
            return False

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == word[0] and self.helper(matrix, word, 1, i, j):
                    return True

        return False

    def helper(self, matrix: list, word: str, index: int, x: int, y: int):
        if index == len(word):
            return True

        m, n = len(matrix), len(matrix[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        next_letter = word[index]
        ans = False

        original = matrix[x][y]
        matrix[x][y] = "_"
        for direction in directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            if 0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] == next_letter:
                ans |= self.helper(matrix, word, index + 1, next_x, next_y)

        matrix[x][y] = original

        return ans








