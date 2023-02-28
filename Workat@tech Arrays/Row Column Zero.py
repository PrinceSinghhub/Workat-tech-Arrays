class Solution:
    def setRowColumnZeroes(self, mat):

        dummy_row = [-1] * len(mat[0])
        dummy_collom = [-1] * len(mat)

        for i in range(len(mat)):
            for j in range(len(mat[i])):

                if mat[i][j] == 0:
                    dummy_row[j] = 0
                    dummy_collom[i] = 0

        # print(dummy_row)
        # print(dummy_collom)

        for i in range(len(mat)):
            for j in range(len(mat[i])):

                if dummy_row[j] == 0 or dummy_collom[i] == 0:
                    mat[i][j] = 0

        # print(mat)
        return mat


