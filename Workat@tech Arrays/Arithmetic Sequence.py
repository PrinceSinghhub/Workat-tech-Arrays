class Solution:
    def isArithmeticSequence(self, arr: List[int]) -> bool:

        arr.sort()

        ans = set()

        for i in range(len(arr) - 1):
            ans.add(arr[i] - arr[i + 1])

        if len(ans) == 1:
            return True
        return False



