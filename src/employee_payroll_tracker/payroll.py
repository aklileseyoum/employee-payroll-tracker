"""Apply tax to a salary, then generate and display the payslip."""

from employee import Employee

def apply_tax(employee: Employee):
    """Return the salary after the tax percentage has been applied."""
    return employee.calculate_salary() * (1 - employee.tax)
    

def generate_payslip(employee: Employee):
    """Fetch the employee's data and display it as an orderly payslip."""

    print("=" * 30)
    print(f"{employee.name:^30}")                   
    print("=" * 30)

    print(f"{'Gross Salary':<15}{(employee.calculate_salary() - employee.bonus):>15,.2f}")   
    print(f"{'Bonus':<15}{(employee.bonus):>15,.2f}")
    print(f"{'Total Salary':<15}{(employee.calculate_salary()):>15,.2f}")
    print(f"{'Tax Percentage':<15}{employee.tax:>15.0%}")
    print(f"{'Net Salary':<15}{apply_tax(employee):>15,.2f}")

    print("-" * 30)
