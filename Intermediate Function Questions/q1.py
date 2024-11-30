def find_largest_number(numbers):
    if not numbers:  
        return "The list is empty"
    return max(numbers)

num_list = list(map(float, input("Enter numbers separated by spaces: ").split()))
largest_number = find_largest_number(num_list)
print(f"The largest number in the list is: {largest_number}")
