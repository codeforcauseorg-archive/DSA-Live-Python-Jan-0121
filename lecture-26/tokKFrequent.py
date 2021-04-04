from heapq import *

def topKFreq(nums, k):

    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    minHeap = []

    for num, frequency in freq.items():
        heappush(minHeap, (frequency, num))
        if len(minHeap) > k:
            # smallest item remove
            heappop(minHeap)

    ans = []
    while minHeap:
        ans.append(heappop(minHeap)[1])

    return ans
