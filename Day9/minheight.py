
arr = [3, 9, 12, 16, 20]
k = 3

# WHAT IS INTITALLY DID

# class Solution:

#     def getMinDiff(self, arr, k):
#         # code here
#         arr.sort()

#         for num in range(len(arr)):
#             if arr[num] <= k:
#                 arr[num] += k
#             else:
#                 arr[num] -= k
#         maxv = max(arr)
#         minv = min(arr)

#         result = maxv-minv
#         print(result)

# the correct solution


def getMinDiff(arr, k):
    n = len(arr)
    arr.sort()

    res = arr[n - 1] - arr[0]
    for i in range(1, len(arr)):

        if arr[i] - k < 0:
            continue
        minH = min(arr[0] + k, arr[i] - k)

        maxH = max(arr[i - 1] + k, arr[n - 1] - k)

        res = min(res, maxH - minH)

    return res


if __name__ == "__main__":
    k = 6
    arr = [12, 6, 4, 15, 17, 10]

    ans = getMinDiff(arr, k)
    print(ans)
