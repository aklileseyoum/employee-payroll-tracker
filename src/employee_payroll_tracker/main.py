"""Run the interactive menu for managing employees and payslips."""

from employee import FullTimeEmployee, ContractEmployee, Intern
from payroll import generate_payslip
from utils import wipe

# Storage for employee records
employees_record = []
employee_lookup = {}
counter = 1

while True:
    # Main menu loop
    wipe()
    print("=" * 60)
    print(f"{'Welcome to Employee Payroll Tracker':^60}")
    print("=" * 60)

    print("Would you like to:")
    print("1. Add new employee")
    print("2. View employee's payslip")
    print("3. exit\n")

    choice = input("Choose: ")

    if choice == "1":
        # Add a new employee
        wipe()
        name = input("Employee's name: ")

        if name == "":
            # Ask again if the name is empty
            print("Wrong input, please try again.\n")
            to_continue = input("\nPress any key to go back or 0 to exit: ")

            if to_continue == "0":
                # Exit the program
                print("\nBye.")
                break
            
            continue

        # Choose the employment type
        print("\n")
        print("=" * 20)
        print("Choose Employment Type")
        print("=" * 20)

        print("1. Full Time Employee")
        print("2. Contract Employee")
        print("3. Intern")

        employee_type = input("Choose: ")

        if employee_type == "1":
            # Create a full-time employee
            employee_object = FullTimeEmployee(name, counter)

        elif employee_type == "2":
            # Create a contract employee
            employee_object = ContractEmployee(name, counter)

        elif employee_type == "3":
            # Create an intern
            employee_object = Intern(name, counter)

        else:
            # Invalid employment type
            print("Wrong input, please try again.\n")
            to_continue = input("\nPress any key to go back or 0 to exit: ")

            if to_continue == "0":
                # Exit the program
                print("\nBye.")
                break

            continue

        # Save the employee in both the list and the dict
        employee_lookup[counter] = employee_object
        employees_record.append(employee_object)

        counter += 1

        print("\nNew Employee Successfully registered.")
        to_continue = input("\nPress any key to go back or 0 to exit: ")

        if to_continue == "0":
            # Exit the program
            print("Bye.")
            break

    elif choice == "2":
        # View an employee's payslip

        if len(employees_record) == 0:
            # Go back if there are no employees yet
            print("\nNo Employees registered yet")
            to_continue = input("\nPress any key to go back or 0 to exit: ")

            if to_continue == "0":
                # Exit the program
                print("Bye.")
                break

            continue

        wipe()
        print("=" * 20)
        print("Name of Existing Employees")
        print("=" * 20)

        for i in range(len(employees_record)):
            # List the registered employees
            print(f"{i+1}. {employees_record[i].name}")

        chosen_employee = input("\nChoose Employee: ")
        if chosen_employee.isdigit() and int(chosen_employee) in employee_lookup:
            # Show the payslip if the employee exists
            print("\n")
            generate_payslip(employee_lookup[int(chosen_employee)])

        else:
            # Employee not found or invalid input
            print("Wrong input, please try again.\n")

        to_continue = input("\nPress any key to go back or 0 to exit: ")

        if to_continue == "0":
            # Exit the program
            print("\nBye.")
            break

    elif choice == "3":
        # Exit the program
        print("\nBye.")
        break

    else:
        # Invalid menu choice
        print("Wrong input, please try again.\n")
        to_continue = input("\nPress any key to go back or 0 to exit: ")

        if to_continue == "0":
            # Exit the program
            print("\nBye.")
            break

        
        

