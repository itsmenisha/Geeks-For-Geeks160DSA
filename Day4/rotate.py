import math
arr = [1, 2, 3, 4, 5]
d = 3
# [3, 4, 5, 1, 2]


class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotateArr(self, arr, d):
        # Your code here
        n = len(arr)
        d %= n
        a = d-1
        b = n-1
        self.reverse(arr, 0, a)
        self.reverse(arr, d, b)
        self.reverse(arr, 0, b)
        print(arr)

 
sol = Solution()
sol.rotateArr(arr, d)


# space complexity= o(1)
# time complexity = o(n)
