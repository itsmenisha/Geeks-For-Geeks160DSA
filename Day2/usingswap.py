class Solution:
    def pushZerosToEnd(self, arr):
        count = 0
        for num in range(len(arr)):
            if arr[num] != 0:
                arr[count], arr[num] = arr[num], arr[count]
                count += 1


# the time complexity for this is better as it usesonly one loop
