def key_with_highest_value(d):
    if not d:
        return "The dictionary is empty"
    return max(d, key=d.get)

my_dict = {
    'a': 5,
    'b': 12,
    'c': 9
}
key = key_with_highest_value(my_dict)
print(f"The key with the highest value is: {key}")