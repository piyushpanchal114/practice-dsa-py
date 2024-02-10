def removeDuplicates(arr, n):
    temp = 0
    count = 0
    for i in arr:
        if temp != i:
            temp = i
            count += 1
    return count
