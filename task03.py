def calculate_tax(salary):
    if salary > 5_000_000:
        tax = salary * 0.20
    else:
        tax = salary * 0.13
    return int(tax)

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    net_salary = salary - tax
    return int(net_salary)

# Misol
salary = 6_000_000
print(f"Soliq: {calculate_tax(salary):,}".replace(",", "_"))
print(f"Sof maosh: {calculate_net_salary(salary):,}".replace(",", "_"))
