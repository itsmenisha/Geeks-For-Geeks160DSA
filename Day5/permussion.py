arr = [2, 4, 1, 7, 5, 0]
# Output: [2, 4, 5, 0, 1, 7]


class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        if pivot == -1:
            arr.reverse()
            return
        for i in range(n-1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
        left, right = pivot+1, n-1
        while left < right:
            arr[right], arr[left] = arr[left], arr[right]
            right -= 1
            left += 1
        print(arr)


sol = Solution()
sol.nextPermutation(arr)
