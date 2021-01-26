# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5, 000 to the
# annual salary by default but also accepts a different raise amount.
# Write a test case for Employee. Write two test methods, test_give_default
# _raise() and test_give_custom_raise(). Use the setUp() method so you don’t
# have to create a new employee instance in each test method. Run your test
# case, and make sure both tests pass.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""
    
    def setUp(self):
        first = "billy"
        last = "bob"
        salary = 10000
        self.employee = Employee(first, last, salary)
    
    def testGiveDefaultRaise(self):
        """Checking default raise is 5000"""
        self.employee.giveRaise()
        self.assertEqual(self.employee.salary, 15000)
        
    def testGiveCustomRaise(self):
        """Checking for custom raise"""
        self.employee.giveRaise(10000)
        self.assertEqual(self.employee.salary, 20000)
        
if __name__ == "__main__":
    unittest.main()
