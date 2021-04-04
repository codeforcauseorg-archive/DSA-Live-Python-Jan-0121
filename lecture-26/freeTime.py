from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Employee:
    def __init__(self, interval, empIndex, intervalIndex):
        self.interval = interval

        # working hours
        self.empIndex = empIndex
        self.intervalIndex = intervalIndex # index of interval in the employee list

    def __let__(self, other):
        return self.interval.start < other.interval.start

def freeTime(intervals):
    if interval is None:
        return []

    result, minHeap = [], []
    # insert the first interval of every employee in heap
    for i in range(len(intervals)):
        heappush(minHeap, Employee(intervals[i][0], i, 0))

    prev = minHeap[0].interval

    while minHeap:

        # smallest start time
        popped = heappop(minHeap)

        if prev.end < popped.interval.start:
            result.append(Interval(prev.end, popped.interval.start))
            prev = popped.interval
        else:
            if prev.end < popped.interval.end:
                prev = popped.interval

        poppedList = intervals[popped.empIndex]
        if len(poppedList) > popped.intervalIndex + 1:
            heappush(minHeap, Employee(poppedList[popped.intervalIndex + 1], popped.empIndex, popped.intervalIndex + 1))

    return result
