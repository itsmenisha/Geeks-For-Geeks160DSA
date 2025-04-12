class Solution:
    def pushZerosToEnd(self, arr):
        count = 0
        for num in range(len(arr)):
            if arr[num] != 0:
                arr[count] = arr[num]
                count += 1

        while count < len(arr):
            arr[count] = 0
            count += 1
