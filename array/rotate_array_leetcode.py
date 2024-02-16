def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return
    n = k % len(nums)
    temp = []
    for i in range(len(nums)-n):
        temp.append(nums[i])
    count = 0
    for i in range(len(nums)-n, len(nums)):
        nums[count] = nums[i]
        count += 1
    for i in temp:
        nums[count] = i
        count += 1
