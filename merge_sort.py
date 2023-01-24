my_array = [11, 21, 1, 73, 32, 24, 90, 75, 6, 47]

def merge_sort(array):
    if len(array) <= 1:
        return
    
    mid = len(array)//2

    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

def merge_two_sorted_lists(a,b,array):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            array[k] = a[i]
            i+=1
        else:
            array[k] = b[j]
            j+=1
            k+=1
    while i < len_a:
        array[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        array[k] = b[j]
        j+=1
        k+=1        

        