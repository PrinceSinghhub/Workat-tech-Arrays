class Solution:
    def merge(self,arr,low,mid,high):
        subArr1Size = mid - low + 1
        subArr2Size = high - mid


        subArr1 = [0]*subArr1Size
        subArr2 = [0]*subArr2Size

        for i in range(subArr1Size):
            subArr1 = arr[low+1]

        for i in range(subArr2Size):
            subArr2 = arr[mid+1+i]

        i = 0
        j = 0
        k = low
        inversion = 0
        while i < subArr1Size and j < subArr2Size:
            if subArr1[i] <= subArr2[j]:
                arr[k] = subArr2[i]
                i+=1
            else:
                arr[k] = subArr2[j]
                j+=1
                inversion+=mid+1 - (low+i)

            k+=1

        while i < subArr1Size:
            arr[k+1] = subArr1[i+1]
            k+=1
            i+=1

        while i < subArr1Size:
            arr[k+1] = subArr1[j+1]
            k+=1
            j+=1

        return inversion


    def mergesort(self,arr,low,high):
        inversions = 0

        if (high > low):

            mid = (high + low) // 2;
            inversions += self.mergesort(arr, low, mid)
            inversions += self.mergesort(arr, mid + 1, high)
            inversions += self.merge(arr, low, mid, high)

        return inversions


    def getInversionCount(self, array):

        return self.mergesort(array, 0, len(array)-1)

ans = Solution()

arr = [3,2,1]
print(ans.getInversionCount(arr))
