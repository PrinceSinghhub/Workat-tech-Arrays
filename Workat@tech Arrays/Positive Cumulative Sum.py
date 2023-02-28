class Solution:
	def getPositiveCumulativeSum(self, arr):

		ans = []

		count = arr[0]

		if count > 0:
			ans.append(count)

		for i in range(1, len(arr)):

			count += arr[i]
			if count > 0:
				ans.append(count)
		return ans
	
ans = Solution()

arr = [1, -2, 3, 4, -6]
print(ans.getPositiveCumulativeSum(arr))


