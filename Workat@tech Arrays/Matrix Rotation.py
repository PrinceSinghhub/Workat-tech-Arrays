class Solution:
    def rotateMatrix(self, matrix):
        ans = []

        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])

            ans.append(temp[::-1])
        return ans



