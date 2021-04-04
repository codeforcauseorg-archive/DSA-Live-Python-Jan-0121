from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x.start)

    rooms = 0
    minHeap = []

    for interval in intervals:
        while(len(minHeap) > 0 and interval.start >= minHeap[0].end):
            heappop(minHeap)

        heappush(minHeap, interval)

        rooms = max(len(minHeap), rooms)

    return rooms
