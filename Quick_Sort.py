def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

user_input = input("Enter a list of numbers separated by spaces: ")
user_list = [int(x) for x in user_input.split()]
sorted_list = quicksort(user_list)
print("Sorted list:", sorted_list)
