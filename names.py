# Testing a function
# using nameFunction.py

from nameFunction import getFormattedName

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    
    last = input("Plase give me a last name: ")
    if last == "q":
        break
    
    formattedName = getFormattedName(first, last)
    print(f"\tNeatly formatted name: {formattedName}.")
    
# Function works, but what if we want to handle middles names? If we add the functionality, we want to make sure that we don't break the way the function handles names that only have a first and last name.

# Unit tests and test cases

# Python's module unittest from the standard library provices tools for testing our code.
# A unit test verifies that one specific aspect of a function's behaviour is correct.
# A test case is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations you expect it to handle.
# A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function.
# It's often good enough to write tests for our code's critical behaviours, and then aim for full coverage only if the project starts to see widespread use.

# See testNameFunction.py