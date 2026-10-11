# Employee Payroll Tracker

A command-line app that registers employees (full-time, contract, intern) and generates payslips. Salary rules differ by employee type, using inheritance and polymorphism.

## Setup

**Requirements:** Python 3.14 or newer.

1. Clone the repository:
```
   git clone <YOUR-REPO-URL>
   cd Employee_Payroll_Tracker
```
2. Install the project:
```
   <FILL IN: the command you used, e.g. your Poetry install command or venv + pip steps>
```

## Usage

Run the program from the project's top folder:

```
python src/employee_payroll_tracker/main.py
```

Menu options:

1. **Add new employee:** enter a name and choose a type (Full Time, Contract, or Intern).
2. **View employee's payslip:** pick a registered employee to see their payslip.
3. **Exit**

Employees are stored in memory only, so they are lost when the program closes.

## Sample Output

```
<FILL IN: paste one payslip from your terminal here>
```

## Project Structure

```
src/employee_payroll_tracker/
├── main.py       # interactive menu
├── employee.py   # Employee base class and child classes
├── payroll.py    # apply_tax() and generate_payslip()
└── utils.py      # helper functions (screen clearing)
```

## Design Notes

- `Employee` is an abstract base class; each child must override `calculate_salary()`.
- Hourly rate, tax rate, and bonus are private values exposed through `@property`, with setters that reject invalid values.

## Debugging

Screenshots of debugging in VS Code (breakpoint, stepping into a method, final payslip) are in the `docs/` folder.