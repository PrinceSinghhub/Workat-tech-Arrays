class Solution:
    def largestContiguousSum(self, arr):

        # optimize Solution

        Max = arr[0]

        currSum = 0

        for i in arr:
            currSum+=i
            if currSum > Max:
                Max = currSum
            if currSum < 0:
                currSum = 0

        return Max


        # brute force Approch
        # myarr = []
        #
        # for i in range(len(arr)):
        #
        #     for j in range(len(arr)):
        #
        #         if (i+1) > len(arr):
        #             break
        #         else:
        #             temp = arr[j:i+1]
        #             if len(temp) > 0:
        #                 myarr.append((sum(temp)))
        #                 # myarr.append((temp))
        # return max(myarr)


ans = Solution()
arr = [4,-6,2,5]
print(ans.largestContiguousSum(arr))





