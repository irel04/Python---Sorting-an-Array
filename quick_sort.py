my_array = [11, 21, 1, 73, 32, 24, 90, 75, 6, 47]

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
