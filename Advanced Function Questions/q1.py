def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result
    return result

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
power_result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {power_result}")
