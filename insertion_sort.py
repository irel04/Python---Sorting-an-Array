def insertion_sort(array):
    for i in range(1, len(array)):
        anchor = array[i]
        j = i - 1
        
        while j >= 0 and anchor < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = anchor


my_array = [11, 21, 1, 73, 32, 24, 90, 75, 6, 47]
insertion_sort(my_array)
print(my_array)
        