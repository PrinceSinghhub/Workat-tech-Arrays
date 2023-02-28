from collections import Counter

# this solution not accept in python Compiler so thats why code in java
class Solution:
    def getIdenticalTwinsCount(self, arr):
        count = Counter(arr)

        ans = 0
        for key, val in count.items():
            if val == 2:
                ans += 1
        return ans

ans = Solution()
arr = [4,1,1,1,1]
print(ans.getIdenticalTwinsCount(arr))




