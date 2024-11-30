def average_salary(salaries):
    if len(salaries) == 0:
        return "The list of salaries is empty."
    return sum(salaries) / len(salaries)

salaries_list = [35000, 45000, 55000, 60000, 70000]
avg_salary = average_salary(salaries_list)
print(f"The average salary is: {avg_salary}")
