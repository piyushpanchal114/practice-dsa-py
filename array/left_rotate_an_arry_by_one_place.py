def rotateArray(arr, n: int):
    last = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = last
    return arr
