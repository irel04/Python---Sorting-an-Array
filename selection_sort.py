def selection_sort(array):

    for i in range(len(array)-1):
        minpos = i
        for j in range(i, len(array)):
            if array[j] < array[minpos]:
                minpos = j

        temp = array[i]
        array[i] = array[minpos]
        array[minpos] = temp

my_array = [11, 21, 1, 73, 32, 24, 90, 75, 6, 47]

selection_sort(my_array)
print(my_array)