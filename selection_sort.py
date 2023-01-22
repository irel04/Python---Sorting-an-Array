def sort(nums):

    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if nums[j] < nums[i]:
                minpos = j

     
