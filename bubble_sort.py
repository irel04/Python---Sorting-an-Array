my_array = [11, 21, 1, 73, 32, 24, 90, 75, 6, 47]

def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

bubble_sort(my_array)
print(my_array)