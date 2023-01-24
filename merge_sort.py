my_array = [11, 21, 1, 73, 32, 24, 90, 75, 6, 47]

def merge_sort(array):
    if len(array) <= 1:
        return
    
    mid = len(array)//2

    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)