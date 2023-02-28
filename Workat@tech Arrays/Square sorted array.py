class Solution:
    def getSquareSortedArray(self, arr):
        # add your logic here

        ans = []
        for i in arr:
            ans.append(pow(i, 2))
        ans.sort()
        return ans


