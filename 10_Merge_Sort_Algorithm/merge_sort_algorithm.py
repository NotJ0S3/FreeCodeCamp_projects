def merge_sort(array):
    """
    Sorts an array in ascending order using the merge sort algorithm.
    The algorithm works by recursively dividing the array into halves,
    sorting each half, and then merging them back together.
    
    Args:
    - array: List of numbers to be sorted.
    """
    if len(array) <= 1:
        # Base case: An array with one or no elements is already sorted.
        return
    
    # Step 1: Find the middle point of the array to divide it into two halves.
    middle_point = len(array) // 2
    left_part = array[:middle_point]   # Left half of the array.
    right_part = array[middle_point:]  # Right half of the array.

    # Step 2: Recursively call merge_sort on both halves to sort them.
    merge_sort(left_part)
    merge_sort(right_part)

    # Step 3: Merge the two sorted halves back together.
    left_array_index = 0  # Pointer for the current index in the left half.
    right_array_index = 0  # Pointer for the current index in the right half.
    sorted_index = 0  # Pointer for the current index in the merged array.

    # Step 4: Compare elements from both halves and insert the smaller one into the array.
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1  # Move to the next element in the left half.
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1  # Move to the next element in the right half.
        sorted_index += 1  # Move to the next position in the merged array.

    # Step 5: Copy any remaining elements from the left half (if any) into the array.
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Step 6: Copy any remaining elements from the right half (if any) into the array.
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    # Define the array to be sorted.
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    
    # Display the unsorted array.
    print('Unsorted array: ')
    print(numbers)
    
    # Call merge_sort to sort the array.
    merge_sort(numbers)
    
    # Display the sorted array.
    print('Sorted array: ' + str(numbers))
