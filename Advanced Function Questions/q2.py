def convert_temperature(value, scale):
    if scale.lower() == "celsius":
        return (value * 9/5) + 32
    elif scale.lower() == "fahrenheit":
        return (value - 32) * 5/9
    else:
        return "Invalid scale. Please use 'Celsius' or 'Fahrenheit'."

temp_value = float(input("Enter the temperature value: "))
scale = input("Enter the scale (Celsius or Fahrenheit): ")
converted_temp = convert_temperature(temp_value, scale)
print(f"The converted temperature is: {converted_temp}")
