# A passing test
# To write a test case for a function, import the unittest module and the function you want to test. Then create a class tha tinherits from unittest.TestCase, and write a series of methods to test different aspects of the function's behaviour.

# Importing unittest and our function we want to test
import unittest
from nameFunction import getFormattedName

# Created a class which contains a series of unit tests for getFormattedName(). The class name can be anything we want but it's good to have it related to the function we are testing, and to use 'Test' in the class name.
# The class must inherit from unittest.TestCase so python knows how to run the tests we are writting.
class NamesTestCase(unittest.TestCase):
    """Tests for 'nameFunction.py"""
    
    # Any method that starts with test will be run automatically when we run the file.
    # Within this test method we call the function we want to test.
    def testFirstLastName(self):
        """Do names like 'Janis Joplin' work?"""
        # Argument to be tested, which we call using arguments as if calling the function normally
        formattedName = getFormattedName("janis", "joplin")

        # The assert methods verify that a result you received matches the result you expected to receive. Because we know our function it supposed to output names in title case, we expect it to do so. So we put our function output, against our expected outcome to see if they match.
        # The line says, “Compare the value in formattedName to the string 'Janis Joplin'. If
        # they are equal as expected, fine. But if they don’t match, let me know
        self.assertEqual(formattedName, "Janis Joplin")
       
# This if block looks at a special variable, __name__, which is set when the program is executed. If this file is being run as the main program, the value of __name__ is set to "__main__". In this case, we call unittest.main(), which runs the test case. When a testing framework imports this file, the value of __name__ won't be "__main__" and this block will not be executed.
# if __name__ == "__main__":
#     unittest.main()

# The output

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK

# The dot on the first line tells us that a single test passed.
# Next line tells us that Python ran ontest, and it look less than 0.001 seconds to run.
# The final "OK" tells us that all unit tests in the test case passed

# A failing test
# Let's modify getFormattedName (in nameFunction.py) so it can handle middles names, but we'll do so in a way that breaks the test (as it only tests first and last)

# The failing test's output

# E
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# ERROR: testFirstLastName(__main__.NamesTestCase)
# Do names like 'Janis Joplin' work?
# ----------------------------------------------------------------------
# Traceback(most recent call last):
#   File "testNameFunction.py", line 18, in testFirstLastName
#   formattedName = getFormattedName("janis", "joplin")
#   fullName = f"{first} {middle} {last}"
# NameError: name 'middle' is not defined

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (errors=1)

# The single 'E' at the start stands for error, which is self-explanatory
# Next we see ERROR:... this tells us the name of the test that failed which is helpful when testing many cases.
# Traceback is the standard info about what went wrong and where
# After we see that one unit test was run
# After that we are told how many errors occurred when running the test case. This appears at the end so we know immediately if there are any errors without having to scroll through the logs.

# Responding to a failed test

# If our test failed, don't change the test, instead fix the code that caused the test to fail. Examine the changes we made to the function, and figure out how those changes broke the desired behaviour.
# In our case we added a mandatory middle name which broke the desired behaviour of getFormattedName(). The best option here is to make the middle name optional.
# To make middle optional, we move the parameter in nameFunction.py to the end, and create an if statement to determine if we need to print a middle name.

# Adding new tests
# Let's modify our above code to include testing for a middle name


class NamesTestCase(unittest.TestCase):
    """Tests for 'nameFunction.py"""

    def testFirstLastName(self):
        """Do names like 'Janis Joplin' work?"""
        formattedName = getFormattedName("janis", "joplin")
        self.assertEqual(formattedName, "Janis Joplin")
        
    def testFirstLastMiddleName(self):
        """Do name like 'Wolfgang Amadeus Mozart' work?"""
        formattedName = getFormattedName("wolfgang", "mozart", "amadeus")
        self.assertEqual(formattedName, "Wolfgang Amadeus Mozart")

if __name__ == "__main__":
    unittest.main()
