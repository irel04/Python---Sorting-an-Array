def sort(nums):

    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [11, 21, 1, 73, 32, 24, 90, 75, 6, 47]

sort(nums)
print(nums)