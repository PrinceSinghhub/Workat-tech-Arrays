class Solution:
    def getMaxConsecutiveOnes(self, arr):

        count = 0
        ans = []

        for i in arr:
            if i == 1:
                count += 1
            else:
                ans.append(count)
                count = 0
        ans.append(count)
        return max(ans)