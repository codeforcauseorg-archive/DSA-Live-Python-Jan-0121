# order agnostic binary search
def bs(arr, target):
    s, e = 0, len(arr) - 1
    isAsc = arr[s] < arr[e]

    while s <= e:
        m = s + (e - s) // 2

        if target == arr[m]:
            return m

        if isAsc:
            if target < arr[m]:
                e = m - 1
            else:
                s = m + 1
        else:
            if target > arr[m]:
                e = m - 1
            else:
                s = m + 1

    return -1

# ceiling of a number
def ceiling(arr, target):
    if target > arr[-1]:
        return -1

    s, e = 0, len(arr) - 1

    while s <= e:
        m = s + (e - s) // 2
        if target < arr[m]:
            e = m - 1
        elif target > arr[m]:
            s = m + 1
        else:
            return m

    return s

# Find range of numbers
def findRange(arr, target):
    res = [-1, -1]
    res[0] = bs(arr, target, False)
    if res[0] != -1:
        result[1] = bs(arr, target, True)
    return result

def bs(arr, target, findRightIndex):
    index = -1
    s, e = 0, len(arr) - 1
    while s <= e:
        m = s + (e - s) // 2
        if target < arr[m]:
            e = m - 1
        elif target > arr[m]:
            s = m + 1
        else:
            # target == arr[m]
            index = m
            if findRightIndex:
                s = m + 1
            else:
                e = m - 1
    return index

# find pivot in bitonic array
def findPivot(arr):
    s, e = 0, len(arr) - 1
    while s < e:
        m = s + (e - s) // 2
        if arr[m] > arr[m+1]:
            # we are in desc part
            e = m
        else:
            s = m + 1

    # here after the loop, s == e
    return e

# make pivot of rotated binary search
# solve rotated binary search with pivot
# solve rotated binary search without pivot
# Q: Find the Rotation Count in Rotated Sorted array
