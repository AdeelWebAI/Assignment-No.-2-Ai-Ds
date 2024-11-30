def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

num_list = list(map(int, input("Enter integers separated by spaces: ").split()))
even_sum = sum_of_even_numbers(num_list)
print(f"The sum of all even numbers in the list is: {even_sum}")
