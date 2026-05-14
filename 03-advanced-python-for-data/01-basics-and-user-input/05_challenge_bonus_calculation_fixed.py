# Challenge: Bonus Calculation with User Input - Fixed Version
# The 2024 bonus KPI calculation is: 1000 + salary * bonus percentage
# Inputs: name, salary, bonus percentage
# Output: total bonus value
# Fixes: empty name validation, invalid input handling, negative bonus validation
BONUS_CONSTANT = 1000

try:
    name = input("Type your first name: ")

    if not name.strip():
        print("Error: name cannot be empty.")
    else:
        salary = float(input("Type your monthly salary: "))
        bonus = float(input("Type your bonus percentage: "))

        if bonus <= 0:
            print("Error: bonus percentage must be greater than zero.")
        elif salary <= 0:
            print("Error: salary must be greater than zero.")
        else:
            total_bonus = BONUS_CONSTANT + salary * bonus
            print(f"Hello {name}! Your total bonus is R${total_bonus:.2f}.")

except ValueError:
    print("Error: invalid input. Please type numbers only for salary and bonus.")