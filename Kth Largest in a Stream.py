import heapq

class Solution:
    def kthLargest(self, arr, k):   # <-- k must be here
        heap = []
        result = []

        for num in arr:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

            if len(heap) < k:
                result.append(-1)
            else:
                result.append(heap[0])

        return result
