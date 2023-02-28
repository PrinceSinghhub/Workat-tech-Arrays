class Solution:
    def getEvenDigitNumbers(self, arr):
        ans = [i for i in arr if len(str(i)) % 2 == 0]
        return ans
    # add your logic here

ans = Solution()
arr = [42, 564, 5775, 34, 123, 454, 1, 5, 45, 3556, 23442]
print(ans.getEvenDigitNumbers(arr))