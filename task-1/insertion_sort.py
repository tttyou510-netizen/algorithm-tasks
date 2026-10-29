def insertion_sort(arr):
    comparisons = 0
    shifts = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        
    return arr, comparisons, shifts


if __name__ == "__main__":
    # Test on a simple list
    numbers = [12, 11, 13, 5, 6]
    print("Original list:", numbers)
    
    sorted_list, comps, shifts = insertion_sort(numbers)
    
    print("Sorted list:  ", sorted_list)
    print("Comparisons:  ", comps)
    print("Shifts:       ", shifts)
