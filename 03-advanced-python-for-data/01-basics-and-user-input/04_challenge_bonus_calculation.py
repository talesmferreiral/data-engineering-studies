# Challenge: Bonus Calculation with User Input
# The 2024 bonus KPI calculation is: 1000 + salary * bonus percentage
# Inputs: name, salary, bonus percentage
# Output: total bonus value

BONUS_CONSTANT = 1000

name = input("Type your first name: ")
salary = float(input("Type your monthly salary: "))
bonus = float(input("Type your bonus percentage: "))

total_bonus = BONUS_CONSTANT + salary * bonus

print(f"Hello {name}! Your total bonus is R${total_bonus:.2f}.")