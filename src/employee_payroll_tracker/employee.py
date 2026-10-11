"""Define the Employee base class and its child classes."""

from abc import ABC, abstractmethod

class Employee(ABC):
    """Base class for all employees, holding the shared private payroll values."""

    _hourly = 20
    _tax = 0.15
    _bonus = 0

    def __init__(self, name, id_no):
        """Save the employee's name and ID."""
        self.name = name
        self.id_no = id_no

    def __str__(self):
        """Return the employee's name as readable text."""
        return f"Employee's name is {self.name}"

    def __repr__(self):
        """Return a developer-friendly description of the employee."""
        return f"{type(self).__name__}(name={self.name}, id={self.id_no})"

    @property
    def hourly(self):
        """Returns the hourly rate."""
        return self._hourly

    @hourly.setter
    def hourly(self, hourly):
        """Set the hourly rate, raises value error if it is zero or less."""
        if hourly <= 0:
            raise ValueError("No negative hourly salary amount")
        
        self._hourly = hourly

    @property
    def tax(self):
        """Returns the tax rate."""
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Set the tax rate; raise ValueError if it is not between 0 and 1."""
        if tax < 0 or tax > 1:
            raise ValueError("Tax input should be between 0 and 1")
        
        self._tax = tax

    @property
    def bonus(self):
        """Returns the bonus."""
        return self._bonus

    @bonus.setter
    def bonus(self, bonus):
        """Set the bonus, raises value error if it is negative."""
        if bonus < 0:
            raise ValueError("No negative bonuses")
        
        self._bonus = bonus

    @abstractmethod
    def calculate_salary(self):
        """Return the salary; every child class must override this."""
        pass


class FullTimeEmployee(Employee):
    """Employee paid for full-time work."""

    _bonus = 1000

    def calculate_salary(self):
        """Return the hourly rate times 40, plus the bonus."""
        return (self.hourly * 40) + self._bonus

class ContractEmployee(Employee):
    """Employee paid for contract work."""

    _bonus = 500

    def calculate_salary(self):
        """Return the hourly rate times 30, plus the bonus."""
        return (self.hourly * 30) + self._bonus

class Intern(Employee):
    """Employee who is an intern."""
    
    def calculate_salary(self):
        """Return the hourly rate times 20."""
        return self.hourly * 20

