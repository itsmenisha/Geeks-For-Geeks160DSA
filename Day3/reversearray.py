arr = [5, 4, 3, 2, 1]


class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        # code here
        for i in range(n // 2):
            # divides the list len in half - if 5 it gives 2 as the 3 in this example reverses to the same position no need to reverse
            temp = arr[i]
            arr[i] = arr[n-i-1]  # last item in first[5-1-0]
            arr[n-i-1] = temp  # first item in last
        print(arr)


sol = Solution()
sol.reverseArray(arr)

# This was the problem that made me understand space and time complexity perfectly
# Very easy to understand
# space complexity= o(1){takes no extra space}
# time complexity = o(n/2) as only iterates to half
