# User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        if n < 2:
            return -1

        first = second = float('-inf')
        for num in arr:
            if num > first:
                second = first
                first = num

            elif first > num > second:
                second = num
        if second == float('-inf'):
            return -1
        else:
            return second
