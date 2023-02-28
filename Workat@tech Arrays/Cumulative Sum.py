class Solution:
    def getCumulativeSum(self, arr):
        ans = []
        total = 0

        for i in arr:
            total += i
            ans.append(total)
        return ans


ans = Solution()
arr = [1, 2, 3, 4]
print(ans.getCumulativeSum(arr))
