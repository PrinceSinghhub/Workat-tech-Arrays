class Solution:

    # this solution not accept in python Compiler so thats why code in java

    def isPrime(self, n):

        count = 2

        while count * count <= n:
            if n % count == 0:
                return False
            count += 1
        return True

    def primesUptoN(self, n):

        if n < 2:
            print()


        else:
            ans = []
            for i in range(2, n + 1):
                if self.isPrime(i):
                    ans.append(i)
            for i in ans:
                print(i, end=" ")

    # add your logic here
ans = Solution()
ans.primesUptoN(20)