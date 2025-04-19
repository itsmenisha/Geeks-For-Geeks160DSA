# Python program to find Maximum Product Subarray using Minimum
# Maximum Product ending at every index

# function to find the product of max product subarray.
def max_product(arr):
    
    n = len(arr)

    # max product ending at the current index
    currMax = arr[0]

    # min product ending at the current index
    currMin = arr[0]

    # Initialize overall max product
    maxProd = arr[0]

    # Iterate through the array
    for i in range(1, n):

        # Temporary variable to store the maximum product ending
        # at the current index
        temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)

        # Update the minimum product ending at the current index
        currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)

        # Update the maximum product ending at the current index
        currMax = temp

        # Update the overall maximum product
        maxProd = max(maxProd, currMax)

    return maxProd


if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    print(max_product(arr))
