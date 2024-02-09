def isSorted(n: int,  a: [int]) -> int: # type: ignore
    i = 1
    while n!=i:
        if a[i-1] > a[i]:
            return 0
        i += 1 
    return 1
