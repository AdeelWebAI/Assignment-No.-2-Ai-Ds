from collections import Counter

def character_frequency(s):
    return dict(Counter(s))

input_string = input("Enter a string: ")
frequency = character_frequency(input_string)
print(f"The frequency of each character is: {frequency}")
