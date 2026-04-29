class Solution:
    def minSwaps(self, arr):
        ones = sum(arr)

        if ones == 0:
            return -1

        # Count zeros in first window
        zeros = arr[:ones].count(0)
        min_swaps = zeros

        # Sliding window
        for i in range(ones, len(arr)):
            if arr[i - ones] == 0:  # outgoing element
                zeros -= 1
            if arr[i] == 0:         # incoming element
                zeros += 1

            min_swaps = min(min_swaps, zeros)

        return min_swaps
