import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

def selection(arr, k):
    if k < 1 or k > len(arr):
        return None
    return quickselect(arr, 0, len(arr) - 1, k - 1)



def main():
    # Example usage:
    arr = [5, 1, 6, 7, 3, 4, 8]
    k = 6
    print(selection(arr, k))  # Output: 4

if __name__ == "__main__":
    main()