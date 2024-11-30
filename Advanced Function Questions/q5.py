def remove_duplicates(lst):
    return list(set(lst))

my_list = [1, 2, 3, 4, 5, 3, 2, 6, 7]
unique_list = remove_duplicates(my_list)
print(f"The list after removing duplicates is: {unique_list}")
