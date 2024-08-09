def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

if __name__ == "__main__":
    print("Enter the elements of the array (space seperated): ")
    arr = list(map(int, input().strip().split()))
    sorted_arr = quicksort(arr)
    print(sorted_arr)
