def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print('pivot ' + str(pivot))
    left = [eachNumber for eachNumber in arr if eachNumber < pivot]
    print('left ' + str(left))
    middle = [eachNumber for eachNumber in arr if eachNumber == pivot]
    print('middle ' + str(middle))
    right = [eachNumber for eachNumber in arr if eachNumber > pivot]
    print('right ' + str(right))
    print('return ' + str(quick_sort(left) + middle + quick_sort(right)))
    return quick_sort(left) + middle + quick_sort(right)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2]
numbers = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
