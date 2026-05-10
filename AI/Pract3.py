def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap after inner loop finishes
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# -------- Multiple Test Cases --------
test_cases = [
    [64, 25, 12, 22, 11],            # Normal case
    [5, 4, 3, 2, 1],                 # Reverse order
    [1, 2, 3, 4, 5],                 # Already sorted
    [3, 3, 2, 1, 2],                 # Duplicates
    [-5, -1, -3, 2, 0],              # Negative numbers
    [10],                            # Single element
    []                               # Empty list
]

for i, data in enumerate(test_cases, 1):
    print(f"Test Case {i}:")
    print("Original:", data)
    print("Sorted  :", selection_sort(data.copy()))
    print("-" * 30)