class Solution:
    def getKthLargestElement(self, arr,k):
        arr.sort()

        return arr[-k]



