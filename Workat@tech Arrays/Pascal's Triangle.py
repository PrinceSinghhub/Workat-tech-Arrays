class Solution:
    def pascalTriangleRow(self, n: int) -> List[int]:
        prev = 1
        nr = [1]
        n = n - 1

        for i in range(1, n + 1):
            curr = (prev * (n - i + 1)) // i
            nr.append(curr)
            prev = curr

        return nr


