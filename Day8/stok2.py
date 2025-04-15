# Python program to minimize the maximum difference
# between heights using Sorting

def getMinDiff(arr, k):
    n = len(arr)
    arr.sort()

    # If we increase all heights by k or decrease all
    # heights by k, the result will be arr[n - 1] - arr[0]
    res = arr[n - 1] - arr[0]

    # For all indices i, increment arr[0...i-1] by k and
    # decrement arr[i...n-1] by k
    for i in range(1, len(arr)):
        # Impossible to decrement height of ith tower by k,
        # continue to the next tower
        if arr[i] - k < 0:
            continue

        # Minimum height after modification
        minH = min(arr[0] + k, arr[i] - k)

        # Maximum height after modification
        maxH = max(arr[i - 1] + k, arr[n - 1] - k)

        # Store the minimum difference as result
        res = min(res, maxH - minH)

    return res


if __name__ == "__main__":
    k = 6
    arr = [12, 6, 4, 15, 17, 10]

    ans = getMinDiff(arr, k)
    print(ans)
